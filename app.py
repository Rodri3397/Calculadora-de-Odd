import streamlit as st

def calcular_ev(handicap, odd, dados):
    match handicap:
        case "Handicap +0.5":
            d, e, v = dados
            return v * (odd - 1) + e * (odd - 1) - d
        case "Handicap +0.25":
            d, e, v = dados
            return v * (odd - 1) + e * ((odd - 1) / 2) - d
        case "Handicap -0.25":
            d, e, v = dados
            return v * (odd - 1) - e * ((odd - 1) / 2) - d
        case "Handicap -0.5":
            d, e, v = dados
            return v * (odd - 1) - e - d
        case "Handicap 0.0":
            d, e, v = dados
            return v * (odd - 1) - d
        case "Handicap +0.75":
            v, e, d1, d2 = dados
            return v * (odd - 1) + e * (odd - 1) - (d1 * 0.5 + d2)
        case "Handicap -0.75":
            d, e, v1, v2 = dados
            return v1 * ((odd - 1) / 2) + v2 * (odd - 1) - e - d
        case "Handicap +1.0":
            v, e, d1, d2 = dados
            return v * (odd - 1) + e * (odd - 1) - d2
        case "Handicap -1.0":
            d, e, v1, v2 = dados
            return v2 * (odd - 1) - e - d

st.title("Calculadora de Valor Esperado (EV) - Handicap Asiático")

handicap_options = [
    "Handicap +0.5", "Handicap +0.25", "Handicap -0.25",
    "Handicap -0.5", "Handicap 0.0", "Handicap +0.75",
    "Handicap -0.75", "Handicap +1.0", "Handicap -1.0"
]

handicap = st.selectbox("Escolha o tipo de handicap:", handicap_options)
odd = st.number_input("Insira a Odd", min_value=1.01, step=0.01)

dados = []

if handicap in ["Handicap +0.5", "Handicap +0.25", "Handicap -0.25", "Handicap -0.5", "Handicap 0.0"]:
    d = st.number_input("Número de derrotas", min_value=0.0)
    e = st.number_input("Número de empates", min_value=0.0)
    v = st.number_input("Número de vitórias", min_value=0.0)
    dados = [d, e, v]

elif handicap in ["Handicap +0.75", "Handicap +1.0"]:
    v = st.number_input("Número de vitórias", min_value=0.0)
    e = st.number_input("Número de empates", min_value=0.0)
    d1 = st.number_input("Derrotas por 1 gol", min_value=0.0)
    d2 = st.number_input("Derrotas por mais de 1 gol", min_value=0.0)
    dados = [v, e, d1, d2]

elif handicap in ["Handicap -0.75", "Handicap -1.0"]:
    d = st.number_input("Número de derrotas", min_value=0.0)
    e = st.number_input("Número de empates", min_value=0.0)
    v1 = st.number_input("Vitórias por 1 gol", min_value=0.0)
    v2 = st.number_input("Vitórias por mais de 1 gol", min_value=0.0)
    dados = [d, e, v1, v2]

if st.button("Calcular EV"):
    resultado = calcular_ev(handicap, odd, dados)
    st.success(f"Valor Esperado (EV): {resultado:.2f}")