from flask import Flask

app = Flask(__name__)

@app.route('/curriculo')
def home():
    return '''
    
<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Meu Currículo Profissional</title>
    
    <!-- O CSS começa aqui -->
    <style>
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background-color: #f0f2f5;
            color: #333;
            line-height: 1.6;
            margin: 0;
            padding: 40px 20px;
        }

        .resume-container {
            max-width: 850px;
            margin: auto;
            background: #ffffff;
            padding: 50px;
            border-radius: 8px;
            box-shadow: 0 4px 15px rgba(0,0,0,0.1);
        }

        header {
            text-align: center;
            border-bottom: 3px solid #1a2a6c;
            padding-bottom: 25px;
            margin-bottom: 30px;
        }

        header h1 {
            margin: 0;
            color: #1a2a6c;
            font-size: 2.2rem;
            text-transform: uppercase;
        }

        .contact-info {
            margin-top: 10px;
            font-size: 0.9rem;
            color: #555;
        }

        h2 {
            color: #1a2a6c;
            border-left: 6px solid #1a2a6c;
            padding-left: 15px;
            text-transform: uppercase;
            font-size: 1.3rem;
            margin-top: 30px;
            background: #f8f9fa;
        }

        .item { 
            margin-bottom: 20px; 
            padding-left: 20px;
        }

        .item h3 { 
            margin: 5px 0; 
            font-size: 1.15rem; 
            color: #2c3e50;
        }

        .item span { 
            font-size: 0.85rem; 
            font-weight: bold;
            color: #e67e22; 
        }

        .skills {
            display: flex;
            flex-wrap: wrap;
            gap: 10px;
            padding-left: 20px;
        }

        .skills span {
            background: #1a2a6c;
            color: white;
            padding: 6px 15px;
            border-radius: 4px;
            font-size: 0.85rem;
        }

        @media print {
            body { background: white; padding: 0; }
            .resume-container { box-shadow: none; width: 100%; max-width: 100%; }
        }
    </style>
</head>
<body>

    <div class="resume-container">
        <header>
            <h1>Arthur Assis dos Santos</h1>
            <p><strong>Desenvolvedor Python | Flask | Backend</strong></p>
            <div class="contact-info">
                <span>📍 São Paulo, SP</span> | 
                <span>📞 (11) 99999-9999</span> | 
                <span>✉️ email@exemplo.com</span>
            </div>
        </header>

        <section>
            <h2>Resumo Profissional</h2>
            <p>Desenvolvedor focado em Python e Flask, com interesse em criar sistemas robustos e escaláveis. Conhecimento em boas práticas de código e ferramentas modernas de desenvolvimento no VS Code.</p>
        </section>

        <section>
            <h2>Experiência Profissional</h2>
            <div class="item">
                <h3>Desenvolvedor Backend (Projetos Freelance)</h3>
                <span>2023 – ATUALMENTE</span>
                <ul>
                    <li>Criação de APIs REST utilizando Flask e Python.</li>
                    <li>Integração de templates HTML dinâmicos.</li>
                </ul>
            </div>
        </section>

        <section>
            <h2>Formação  Acadêmica</h2>
            <div class="item">
                <h3>Análise e Desenvolvimento de Sistemas</h3>
                <span>EM ANDAMENTO</span>
            </div>
        </section>

        <section>
            <h2>Habilidades Técnicas</h2>
            <div class="skills">
                <span>Python</span>
                <span>Flask</span>
                <span>HTML5 / CSS3</span>
                <span>Git & GitHub</span>
                <span>SQL Server</span>
                <span>VS Code</span>
            </div>
        </section>
    </div>

</body>
</html>       
    '''

if __name__ == '__main__':
    app.run(debug=True)