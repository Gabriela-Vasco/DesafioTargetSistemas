import json

def load_daily_revenue_from_json(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
        daily_revenue = data["faturamento_diario"]
        # Convertendo os valores para inteiros
        daily_revenue = [int(revenue) for revenue in daily_revenue]
    return daily_revenue

def calculate_statistics(daily_revenue):
    total_revenue = sum(daily_revenue)
    days_with_revenue_above_average = sum(1 for revenue in daily_revenue if revenue > total_revenue / len(daily_revenue))
    return min(daily_revenue), max(daily_revenue), days_with_revenue_above_average

def main():
    # Carregar os dados do faturamento diário de um arquivo JSON
    file_path = "faturamento_mensal.json"
    daily_revenue = load_daily_revenue_from_json(file_path)

    # Calcular estatísticas
    min_revenue, max_revenue, days_above_average = calculate_statistics(daily_revenue)

    # Imprimir resultados
    print(f"Menor valor de faturamento diário: R${min_revenue}")
    print(f"Maior valor de faturamento diário: R${max_revenue}")
    print(f"Número de dias com faturamento acima da média mensal: {days_above_average}")

if __name__ == "__main__":
    main()
