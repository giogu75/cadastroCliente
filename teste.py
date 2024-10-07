import streamlit as st
import pandas as pd
import numpy as np

# Cria um DataFrame pandas com dados aleatórios
df = pd.DataFrame(
    np.random.randn(10, 5),
    columns=('col %d' % i for i in range(5))
)

# Converte o DataFrame para HTML sem a coluna de índice
html_table = df.to_html(index=False)

# Exibe o DataFrame formatado em HTML
st.markdown(html_table, unsafe_allow_html=True)
