import streamlit as st

# 1. Configuração da página (Deve ser a primeira linha Streamlit)
st.set_page_config(
    page_title="Processamento de Dados & Automação para PME",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# 2. CSS Personalizado para Design Minimalista e Responsividade
st.markdown("""
    <style>
        /* Esconde elementos padrão da interface do Streamlit */
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        header {visibility: hidden;}
        
        /* Ajuste de espaçamento global */
        .block-container {
            padding-top: 2rem;
            padding-bottom: 2rem;
            max-width: 900px;
        }
        
        /* Tipografia e Estilo */
        h1, h2, h3 {
            font-family: 'Segoe UI', Roboto, sans-serif;
            color: #1E293B;
            font-weight: 600;
        }
        
        .sub-header {
            color: #475569;
            font-size: 1.15rem;
            line-height: 1.6;
            margin-bottom: 2rem;
        }
        
        /* Destaques de Serviços */
        .service-card {
            background-color: #F8FAFC;
            border: 1px solid #E2E8F0;
            border-radius: 8px;
            padding: 1.5rem;
            margin-bottom: 1rem;
        }
        
        /* Botão de Contato Estilizado */
        .stButton>button {
            width: 100%;
            background-color: #2563EB;
            color: white;
            border-radius: 6px;
            padding: 0.75rem 1.5rem;
            font-weight: 600;
            border: none;
            transition: background-color 0.2s;
        }
        
        .stButton>button:hover {
            background-color: #1D4ED8;
            color: white;
        }
    </style>
""", unsafe_allow_html=True)

# 3. Cabeçalho / Hero Section
st.title("Transforme seus Dados em Eficiência Operacional")
st.markdown(
    "<p class='sub-header'>"
    "Ajudamos pequenas e médias empresas a eliminar tarefas manuais, organizar fluxos de dados "
    "e estruturar informações para decisões mais rápidas e seguras."
    "</p>", 
    unsafe_allow_html=True
)

st.divider()

# 4. Seção de Serviços + Imagem 1
st.header("Nossas Soluções")

col1, col2 = st.columns([1, 1], gap="large")

with col1:
    # Espaço reservado para a primeira imagem explicativa (ex: Painel/Dashboard ou Automação)
    st.image(
        "https://images.unsplash.com/photo-1551288049-bebda4e38f71?auto=format&fit=crop&w=800&q=80",
        caption="Visualização e Organização de Dados",
        use_container_width=True
    )

with col2:
    st.markdown("""
    ### O que fazemos pela sua empresa:
    
    * **Automação de Rotinas:** Elimine a digitação manual de dados entre sistemas e planilhas.
    * **Tratamento e Limpeza de Dados:** Padronização de bases de clientes, vendas e estoques.
    * **Relatórios Automatizados:** Receba resumos operacionais prontos direto no seu e-mail ou WhatsApp.
    * **Integração de Sistemas:** Conectamos suas ferramentas para trabalharem em sintonia.
    """)

st.divider()

# 5. Casos de Uso / Aplicação Prática + Imagem 2
st.header("Como Ajudamos Seu Negócio a Crescer")

col3, col4 = st.columns([1, 1], gap="large")

with col3:
    st.markdown("""
    ### Eficiência para o dia a dia
    
    Pequenas empresas perdem dezenas de horas semanais organizando arquivos e cruzando tabelas. 
    
    Nossos serviços estruturam seus dados desde a coleta até a análise, permitindo que sua equipe foque no que realmente importa: **atender bem e vender mais**.
    """)

with col4:
    # Espaço reservado para a segunda imagem (ex: Processamento/Infraestrutura simplificada)
    st.image(
        "https://images.unsplash.com/photo-1460925895917-afdab827c52f?auto=format&fit=crop&w=800&q=80",
        caption="Fluxos de Trabalho Automatizados",
        use_container_width=True
    )

st.divider()

# 6. Seção de Contato
st.header("Entre em Contato")
st.write("Agende uma conversa rápida sem compromisso para analisarmos as necessidades da sua empresa.")

contact_col1, contact_col2 = st.columns([1, 1])

with contact_col1:
    with st.form(key="contact_form"):
        nome = st.text_input("Nome completo")
        empresa = st.text_input("Nome da sua empresa")
        email = st.text_input("E-mail corporativo ou WhatsApp")
        mensagem = st.text_area("Como podemos ajudar?")
        
        submit_button = st.form_submit_button(label="Enviar Mensagem")
        
        if submit_button:
            if nome and email and mensagem:
                st.success("Obrigado pelo contato! Retornaremos em breve.")
            else:
                st.warning("Por favor, preencha os campos obrigatórios (Nome, E-mail e Mensagem).")

with contact_col2:
    st.markdown("""
    <div style='background-color: #F8FAFC; padding: 1.5rem; border-radius: 8px; border: 1px solid #E2E8F0;'>
        <h4>Outros Canais de Atendimento</h4>
        <p><strong>E-mail:</strong> contato@suaempresa.com.br</p>
        <p><strong>WhatsApp:</strong> (00) 90000-0000</p>
        <p><strong>Atendimento:</strong> Segunda a Sexta, das 08h às 18h</p>
    </div>
    """, unsafe_allow_html=True)