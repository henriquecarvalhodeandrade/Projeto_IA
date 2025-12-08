# ============================================================
# Script de análise do modelo YOLO (.pt)
# Autor: ChatGPT
# ============================================================

import os
from ultralytics import YOLO
import torch

OUTPUT_DIR = "analise_modelo"

def preparar_pasta():
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    print(f"📁 Pasta '{OUTPUT_DIR}' criada/aberta com sucesso!\n")


def carregar_modelo(model_path):
    print("🔍 Carregando modelo:", model_path)
    model = YOLO(model_path)
    print("✔ Modelo carregado!\n")
    return model


def analisar_arquitetura(model):
    print("🏗️ Arquitetura do modelo:\n")
    model.info(verbose=True)

    # Salvar arquitetura em arquivo
    with open(os.path.join(OUTPUT_DIR, "arquitetura.txt"), "w") as f:
        f.write(str(model.model))

    print("\n✔ Arquitetura salva em 'arquitetura.txt'\n")


def avaliar_metricas(model):
    print("📊 Avaliando métricas...")
    metrics = model.val(save_json=True)
    
    # Salvar métricas como texto
    with open(os.path.join(OUTPUT_DIR, "metricas.txt"), "w") as f:
        f.write(str(metrics.results_dict))

    print("✔ Métricas salvas em 'metricas.txt'")

    # TENTAR gerar matriz de confusão
    print("📈 Salvando gráficos da avaliação...")

    # Matriz de confusão (diferentes versões do Ultralytics)
    try:
        metrics.plot_confusion_matrix(save_dir=OUTPUT_DIR)
        print("✔ Matriz de confusão salva!")
    except:
        print("⚠️ Métrica nativa indisponível, usando função alternativa...")

        try:
            from ultralytics.utils.plotting import plot_confusion_matrix
            plot_confusion_matrix(metrics.confusion_matrix,
                                  names=model.names,
                                  save_dir=OUTPUT_DIR)
            print("✔ Matriz de confusão salva!")
        except Exception as e:
            print("❌ Erro ao gerar matriz de confusão:", e)

    # Curvas PR
    try:
        metrics.plot_pr_curve(save_dir=OUTPUT_DIR)
        print("✔ Curva PR salva!")
    except:
        print("⚠️ Curva PR não pôde ser gerada.")

    # Gráficos de treino (loss etc.)
    try:
        metrics.plot_results(save_dir=OUTPUT_DIR)
        print("✔ Resultados (loss) salvos!")
    except:
        print("⚠️ Gráfico de loss não disponível.")

    print("\n✔ Avaliação completa!\n")



def rodar_inferencia(model, pasta_val):
    print("🖼️ Rodando inferência nas imagens de validação...")
    results = model.predict(source=pasta_val, save=True, project=OUTPUT_DIR, name="inferencias", conf=0.25)

    print("✔ Inferências salvas na pasta 'analise_modelo/inferencias/'\n")


def converter_para_onnx(model):
    print("\n🔁 Convertendo para ONNX...")

    try:
        model.export(format="onnx")
        print("✔ Modelo exportado para ONNX!")
    except Exception as e:
        print("❌ Falha ao exportar para ONNX:")
        print(e)
        print("\n💡 Sugestão: instale 'onnxscript' ou use Python 3.10/3.11 para evitar problemas.")



def ler_raw_pesos(model_path):
    print("📦 Lendo pesos brutos do arquivo .pt...")
    state = torch.load(model_path, map_location="cpu")

    with open(os.path.join(OUTPUT_DIR, "conteudo_bruto_pt.txt"), "w") as f:
        for key in state.keys():
            f.write(f"{key}\n")

    print("✔ Lista de chaves dos pesos salva em 'conteudo_bruto_pt.txt'\n")


def main():
    preparar_pasta()

    model_path = "best.pt"   # ajuste aqui se seu arquivo tem outro nome
    pasta_val = "datasets/bra-dataset/images/val"

    model = carregar_modelo(model_path)
    analisar_arquitetura(model)
    avaliar_metricas(model)
    rodar_inferencia(model, pasta_val)
    converter_para_onnx(model)
    ler_raw_pesos(model_path)

    print("\n🎉 Análise completa! Todos os resultados estão em:", OUTPUT_DIR)


if __name__ == "__main__":
    main()
