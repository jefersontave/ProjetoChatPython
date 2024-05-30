import flet as ft 

def main(pagina): 
    texto = ft.Text("Chat do Jeff")b
    def enviar_mensagem_tunel(mensagem):
        # Adcionar mensagem no site
        texto_entrada = ft.Text(mensagem)
        chat.controls.append(texto_entrada)
        pagina.update()
    pagina.pubsub.subscribe(enviar_mensagem_tunel)

    def enviar_mensagem(evento):
        pagina.pubsub.send_all(f"{nome_do_usuario.value}: {campo_mensagem.value}")
        # limpe o campo mensagem
        campo_mensagem.value = ""
        pagina.update()

    chat = ft.Column()
    campo_mensagem = ft.TextField(label="Digite sua mensagem", on_submit=enviar_mensagem)
    botao_de_enviar_mensagem = ft.ElevatedButton("Enviar", on_click=enviar_mensagem)
    linha = ft.Row([campo_mensagem,botao_de_enviar_mensagem])

    def entrar_no_chat(evento):
        # fechar o popup
        popup.open = False
        # tirar o titulo
        pagina.remove(texto)
        # tirar o botao
        pagina.remove(botao_iniciar)
        pagina.add(chat)
        pagina.pubsub.send_all(f"{nome_do_usuario.value} entrou no chat não rastreável")
        pagina.add(linha)

        pagina.update()

    titulo_popup = ft.Text("Chat não rastreável")
    nome_do_usuario = ft.TextField(label="Escreva seu nome no chat:")
    botao_entrar_no_chat = ft.ElevatedButton("Entrar no chat", on_click=entrar_no_chat)
    popup = ft.AlertDialog(open=False,
                           modal=True,
                           title=titulo_popup,
                           content=nome_do_usuario,
                           actions=[botao_entrar_no_chat]
                           )

    def abrir_popup(evento):
        pagina.dialog = popup
        popup.open = True
        pagina.update()

    botao_iniciar = ft.ElevatedButton("Iniciar chat", on_click=abrir_popup)

    pagina.add(texto)
    pagina.add(botao_iniciar)
    
ft.app(target=main, view= ft.WEB_BROWSER)
