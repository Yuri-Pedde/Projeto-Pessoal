import pandas as pd  # Importa a biblioteca pandas e a renomeia como pd
import streamlit as st # Importa a biblioteca streamlit e a renomeia como st
from streamlit_gsheets import GSheetsConnection

pd.options.display.max_columns=None
st.set_page_config(
    page_title="Form",
    page_icon="🌍",
    layout="wide",
    initial_sidebar_state='collapsed')

def reset():
    # Função para redefinir o estado da sessão
    # Comentários abaixo são comentários de código, não estão habilitados no momento devido ao formato da entrada.
    # conn.update(
    #         worksheet="dados_form",
    #         data=df,
    #     )
    for key in st.session_state.keys():
        # Itera sobre as chaves do estado da sessão e redefine seus valores para None
        st.session_state[key] = None
        
container_titulo = st.container()       
with container_titulo:
    coluna_inicial1,coluna_inicial2,coluna_inicial3 = st.columns([1,8,1])

    with coluna_inicial2:
        st.markdown(f'<h1 style="text-align: center;color:#FFFFFF;font-size:42px;">{"FORMULÁRIO VIGIAGUA - VIGIDESASTRES"}</h1>', unsafe_allow_html=True)    
        st.markdown(f'<h1 style="text-align: center;color:#FFFFFF;font-size:24px;">{"CRS/CEVS/Secretaria de Saúde do Estado do Rio Grande do Sul"}</h1>', unsafe_allow_html=True)
st.write('<hr style="border: 0; height: 4px; background-color: white; margin: 0 auto;">', unsafe_allow_html=True)
st.write('<div style="margin: 20px;"></div>', unsafe_allow_html=True)
conn = st.experimental_connection("gsheets", type=GSheetsConnection)
# Lê os dados de um arquivo Excel online
dados = conn.read(worksheet='Tabela1', usecols=list(range(14)))

container_Sbox = st.container()
col1,colcenter2,col3 = st.columns([2,1,2])
# Cria um seletor para escolher a Regional de Saúde
with container_Sbox:
    with colcenter2:
        crs = st.selectbox('COORDENADORIA REGIONAL DE SAÚDE', options=sorted(dados['Regional de Saúde'].unique()), index=None, placeholder='Selecione uma CRS', key='crs')
        
        # Cria um seletor para escolher o município com base na Regional de Saúde selecionada
        municipio = st.selectbox('MUNICÍPIO', options=sorted(dados[dados['Regional de Saúde']==crs]['Município'].unique()), index=None, placeholder='Selecione uma município', key='municipio')
        
        # Cria um seletor para escolher o tipo da forma de abastecimento com base no município selecionado
        tipo_forma_abastecimento = st.selectbox('TIPO DA FORMA DE ABASTECIMNENTO', options=sorted(dados[dados['Município']==municipio]['Tipo da Forma de Abastecimento'].unique()), index=None, placeholder='Selecione um tipo de forma de abastecimento', key='forma')

        st.markdown(
            f"""
            <style>
            #root > div:nth-child(1) > div.withScreencast > div > div > div > section > div.block-container.st-emotion-cache-1jicfl2.ea3mdgi5 > div > div > div > div.st-emotion-cache-ocqkz7.e1f1d6gn5 > div:nth-child(2) {{
                box-shadow: 0px 0px 5px 10px rgba(225, 225, 225, 0.3);
                border: 2px solid white;
                border-radius: 15px;
                padding: 15px;
            }}
            </style>
            """,
            unsafe_allow_html=True
            
        )        
        st.markdown(
            f"""
            <style>
            #root > div:nth-child(1) > div.withScreencast > div > div > div > section > div.block-container.st-emotion-cache-1jicfl2.ea3mdgi5 > div > div > div > div.st-emotion-cache-ocqkz7.e1f1d6gn5 > div:nth-child(2) > div > div > div > div:nth-child(1) > div > div {{
                border: 1px solid white; /* Borda verde */
                border-radius: 10px;
                padding: 0px;
                max-width: calc(100% - 25px);
                margin-left: 10px;
            }}
            </style>
            <style>
            #root > div:nth-child(1) > div.withScreencast > div > div > div > section > div.block-container.st-emotion-cache-1jicfl2.ea3mdgi5 > div > div > div > div.st-emotion-cache-ocqkz7.e1f1d6gn5 > div:nth-child(2) > div > div > div > div:nth-child(2) > div > div {{
                border: 1px solid white;
                border-radius: 10px;
                padding: 0px;
                max-width: calc(100% - 25px);
                margin-left: 10px;
            }}
            </style>
            <style>
            #root > div:nth-child(1) > div.withScreencast > div > div > div > section > div.block-container.st-emotion-cache-1jicfl2.ea3mdgi5 > div > div > div > div.st-emotion-cache-ocqkz7.e1f1d6gn5 > div:nth-child(2) > div > div > div > div:nth-child(3) > div > div {{
                border: 1px solid white; /* Borda verde */
                border-radius: 10px;
                padding: 0px;
                max-width: calc(100% - 25px);
                margin-left: 10px;
            }}
            </style>
            """,
            unsafe_allow_html=True
        )
        st.markdown(
            f"""
            <style>
            #root > div:nth-child(1) > div.withScreencast > div > div > div > section > div.block-container.st-emotion-cache-1jicfl2.ea3mdgi5 > div > div > div > div.st-emotion-cache-ocqkz7.e1f1d6gn5 > div:nth-child(2) > div > div > div > div:nth-child(1) > div > label {{
                text-align: center;
                margin: 0 auto; /* Centraliza horizontalmente */
                display: table;
            }}
            </style>
            <style>
            #root > div:nth-child(1) > div.withScreencast > div > div > div > section > div.block-container.st-emotion-cache-1jicfl2.ea3mdgi5 > div > div > div > div.st-emotion-cache-ocqkz7.e1f1d6gn5 > div:nth-child(2) > div > div > div > div:nth-child(2) > div > label {{
                text-align: center;
                margin: 0 auto; /* Centraliza horizontalmente */
                display: table;
            }}
            </style>
            <style>
            #root > div:nth-child(1) > div.withScreencast > div > div > div > section > div.block-container.st-emotion-cache-1jicfl2.ea3mdgi5 > div > div > div > div.st-emotion-cache-ocqkz7.e1f1d6gn5 > div:nth-child(2) > div > div > div > div:nth-child(3) > div > label {{
                text-align: center;
                margin: 0 auto; /* Centraliza horizontalmente */
                display: table;
            }}
            </style>
            """,
            unsafe_allow_html=True
        )

        # Filtra os dados para exibir apenas as informações relevantes com base no município e tipo da forma de abastecimento selecionados
        dados_municipio = dados[(dados['Município']==municipio)&(dados['Tipo da Forma de Abastecimento']==tipo_forma_abastecimento)][['Município','Código Forma de abastecimento','Nome da Forma de Abastecimento', 'Situação']]
        #dados_municipio = pd.concat([dados_municipio, pd.DataFrame({'Município':[municipio, municipio], 'Código Forma de abastecimento':['', ''], 
        #                                                           'Nome da Forma de Abastecimento':['IGNORAR','IGNORAR'], 'Situação':['Funcionando','Parada/danificada']})])
        #dados_municipio['Situação'] = dados_municipio['Situação'].astype("category")
        
st.markdown(f'<h1 style="text-align: center;color:#FFFFFF;font-size:16px;">{"Marque o status de cada uma para informar seu status"}</h1>', unsafe_allow_html=True)# Exibe uma mensagem para o usuário

opcoes_situacao = ['Sem informação', 'Funcionando', 'Parada/danificada']      
container_data_editor = st.container()
with container_data_editor:
    col4,colcenter5,col6 = st.columns([2,1,2])
    try:
        # Tenta executar as seguintes instruções
        # Comentários abaixo são comentários de código, não estão habilitados no momento devido ao formato da entrada.
        # st.subheader(f'{tipo_forma_abastecimento} no município de {municipio}')
        with colcenter5:
            #edited_df = st.data_editor(dados_municipio[['Nome da Forma de Abastecimento','Código Forma de abastecimento','Situação']].set_index('Código Forma de abastecimento'),
             #                          use_container_width=True, hide_index=True, column_config={"category":st.column_config.SelectboxColumn("Situação",default='Sem informação',options=['Sem informação','Funcionando','Parada/danificada'], width='medium'),
              #                                                                                   'category':st.column_config.Column(label='Nome',width='medium')})
            
            quantos_selectbox=0
            def renderizar_editor(dados_x):
                # Cria uma coluna para cada entrada
                for i in range(len(dados_x)):
                    with st.container():
                        # Usando uma selectbox para cada linha e atualizando o valor no DataFrame
                        situacao_atualizada = st.selectbox(dados_x.iloc[i]['Nome da Forma de Abastecimento'],options=opcoes_situacao,
                                                           index=opcoes_situacao.index(dados_x.iloc[i]['Situação']) if dados_x.iloc[i]['Situação'] in opcoes_situacao else 0,
                                                           key=f'situacao_{i}')
                        
                        dados_x.at[i, 'Situação'] = situacao_atualizada
                return dados_x
            dados_atualizados = renderizar_editor(dados_municipio)
            dados_atualizados.dropna(how='any', inplace=True)
            quantos_selectbox = len(dados_atualizados)
            st.write(dados_atualizados.situacao_1)
            st.markdown(f"""
                        <style>
                        #root > div:nth-child(1) > div.withScreencast > div > div > div > section > div.block-container.st-emotion-cache-1jicfl2.ea3mdgi5 > div > div > div > div:nth-child(8) > div > div > div > div.st-emotion-cache-j5r0tf.e1f1d6gn3 > div > div > div > div.st-emotion-cache-0.e1f1d6gn0 > div > div > div > div  
                            {{    
                                box-shadow: 0px 0px 5px 5px rgba(255, 255, 255, 0.25);
                                border: 2px solid white;
                                border-radius: 15px;
                                padding: 15px;
                            }}
                        </style>
                            """, unsafe_allow_html=True)
                                                                                                                                                                                                                                                                                                                                                                                      
            # Cria um botão para enviar a atualização e redefine o estado da sessão quando clicado           
            submit = st.button('Enviar atualização!', type='primary')#, on_click=reset)
            
            st.markdown(f'''
            <style>
            #root > div:nth-child(1) > div.withScreencast > div > div > div > section > div.block-container.st-emotion-cache-1jicfl2.ea3mdgi5 > div > div > div > div:nth-child(8) > div > div > div > div.st-emotion-cache-j5r0tf.e1f1d6gn3 > div > div > div > div:nth-child({str(2+quantos_selectbox)}) > div           
            {{
                display: flex;
                justify-content: center; /* Centraliza horizontalmente */
                align-items: center;
            }}
            </style>
            ''', unsafe_allow_html=True)
            mudancas = pd.DataFrame(columns=['Nome da Forma de Abastecimento', 'Coluna', 'Antes', 'Depois'])
            colunas = ['Sem informação', 'Funcionando', 'Parada/danificada']
            # Verifica se o botão de envio foi clicado
            if submit:
                dados_antigos = dados.copy()
                dados.reset_index(drop=True, inplace=True)
                dados.set_index('Código Forma de abastecimento', inplace=True)
                dados_atualizados.set_index('Código Forma de abastecimento', inplace=True)
                dados.update(dados_atualizados)
                dados.reset_index(inplace=True)
                data_to_send = dados.copy()
                st.table(data_to_send)
                for idx in data_to_send.index:
                    if idx in dados_antigos.index and not dados_antigos.loc[idx].equals(data_to_send.loc[idx]):
                        for coluna in colunas:
                            valor_antigo = dados_antigos.at[idx, coluna]
                            valor_novo = data_to_send.at[idx, coluna]
                            if valor_antigo != valor_novo:
                                # Armazenando detalhes da mudança
                                mudanca = {
                                    'Nome da Forma de Abastecimento': [data_to_send.at[idx,'Nome da Forma de Abastecimento']],
                                    'Coluna': coluna,
                                    'Antes': valor_antigo,
                                    'Depois': valor_novo
                                }
                                mudancas = pd.concat([mudancas, pd.DataFrame([mudanca])], ignore_index=True)

                # Atualizar a planilha
                conn.update(worksheet='Tabela1', data=data_to_send)
                    
                # Exibe uma mensagem de sucesso quando a atualização é enviada
                st.success(f'Atualização enviada! Foram realizadas {len(mudancas)} atualizações!', icon="✅")
                st.markdown(f"""
                <style>
                #root > div:nth-child(1) > div.withScreencast > div > div > div > section > div.block-container.st-emotion-cache-1jicfl2.ea3mdgi5 > div > div > div > div:nth-child(5) > div > div > div > div.st-emotion-cache-fplge5.e1f1d6gn3 > div > div > div > div:nth-child(5)
                {{
                    display: flex;
                    justify-content: center; /* Centraliza horizontalmente */
                    align-items: center;
                    text-align: center;
                }}
                </style>
                <style>
                #root > div:nth-child(1) > div.withScreencast > div > div > div > section > div.block-container.st-emotion-cache-1jicfl2.ea3mdgi5 > div > div > div > div:nth-child(5) > div > div > div > div.st-emotion-cache-keje6w.e1f1d6gn3 > div > div > div > div:nth-child(5) > div > div > div > div
                {{text-align:center;}}
                </style>
                """, unsafe_allow_html=True)
                    
                #mudancas = mudancas.set_index('Nome da Forma de Abastecimento')
                st.dataframe(mudancas.set_index('Nome da Forma de Abastecimento'), use_container_width=True)
                st.markdown(f"""
                <style>            
                #root > div:nth-child(1) > div.withScreencast > div > div > div > section > div.block-container.st-emotion-cache-1jicfl2.ea3mdgi5 > div > div > div > div:nth-child(5) > div > div > div > div.st-emotion-cache-fplge5.e1f1d6gn3 > div > div > div > div:nth-child(2) > div > div                
                {{    
                    display: flex;
                    justify-content: center; /* Centraliza horizontalmente */
                    align-items: center;
                    text-align:center;
                }}    
                </style>
                """, unsafe_allow_html=True)
                st.cache_data.clear()  # Limpa o cache de dados
                                
    except Exception as erro_ultimo:
        # Se ocorrer uma exceção, exibe uma mensagem em branco
        st.write(erro_ultimo)
    opcoes_situacao = ['Sem informação', 'Funcionando', 'Parada/danificada']

# Função para renderizar e atualizar as seleções

