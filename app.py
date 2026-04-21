from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return """
    <!DOCTYPE html>
    <html lang="uk">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Alla | Creative Designer</title>
        <style>
            :root {
                --bg: #080808;
                --accent: #ffffff;
                --secondary: #121212;
                --text-gray: #888;
                --border: rgba(255, 255, 255, 0.08);
            }

            @keyframes reveal {
                from { opacity: 0; transform: translateY(20px); filter: blur(5px); }
                to { opacity: 1; transform: translateY(0); filter: blur(0); }
            }

            * { margin: 0; padding: 0; box-sizing: border-box; font-family: 'Inter', sans-serif; }
            
            body {
                background-color: var(--bg);
                color: var(--accent);
                display: flex;
                justify-content: center;
                min-height: 100vh;
                padding: 40px 20px;
            }

            .container { width: 100%; max-width: 420px; text-align: center; }

            .avatar {
                width: 80px; height: 80px; border-radius: 50%;
                background: linear-gradient(145deg, #1a1a1a, #000);
                margin: 0 auto 20px; border: 1px solid var(--border);
                display: flex; justify-content: center; align-items: center;
                font-size: 24px; font-weight: 300;
            }

            h1 { font-size: 32px; font-weight: 700; letter-spacing: -1px; animation: reveal 0.6s ease; }
            .subtitle { 
                color: var(--text-gray); font-size: 10px; text-transform: uppercase; 
                letter-spacing: 4px; margin-bottom: 40px; animation: reveal 0.6s ease 0.1s backwards;
            }

            .section-title {
                font-size: 12px; color: var(--text-gray); text-transform: uppercase;
                letter-spacing: 2px; margin: 30px 0 15px; display: block;
                animation: reveal 0.6s ease 0.2s backwards;
            }

            .links { display: flex; flex-direction: column; gap: 12px; }

            .btn-main {
                background: var(--accent); color: var(--bg); padding: 18px;
                border-radius: 20px; text-decoration: none; font-weight: 700;
                transition: 0.3s; animation: reveal 0.6s ease 0.3s backwards;
            }

            /* Картки портфоліо */
            .portfolio-grid { display: flex; flex-direction: column; gap: 15px; }

            .work-card {
                background: var(--secondary);
                border: 1px solid var(--border);
                border-radius: 24px;
                padding: 20px;
                text-align: left;
                text-decoration: none;
                color: white;
                transition: 0.4s cubic-bezier(0.2, 1, 0.3, 1);
                animation: reveal 0.8s ease backwards;
            }

            .work-card:hover {
                transform: translateY(-5px) scale(1.02);
                border-color: rgba(255,255,255,0.2);
                background: #181818;
            }

            .work-tag { font-size: 9px; color: var(--text-gray); text-transform: uppercase; letter-spacing: 1px; }
            .work-name { font-size: 16px; font-weight: 600; margin: 4px 0 8px; display: block; }
            .work-desc { font-size: 13px; color: #666; line-height: 1.4; }

            /* Прайс */
            .price-list {
                background: rgba(255,255,255,0.03); border-radius: 24px;
                padding: 20px; border: 1px solid var(--border); text-align: left;
                margin-top: 20px; animation: reveal 0.6s ease 0.7s backwards;
            }

            .price-item {
                display: flex; justify-content: space-between; padding: 10px 0;
                font-size: 14px; border-bottom: 1px solid rgba(255,255,255,0.03);
            }
            .price-item:last-child { border-bottom: none; }
        </style>
    </head>
    <body>
        <div class="container">
            <div class="avatar">A</div>
            <h1>Алла</h1>
            <div class="subtitle">Digital Experience Designer</div>
            
            <div class="links">
                <a href="https://t.me/exlwr" class="btn-main">Замовити проєкт</a>
            </div>

            <span class="section-title">Портфоліо</span>
            <div class="portfolio-grid">
                <div class="work-card" style="animation-delay: 0.4s;">
                    <span class="work-tag">E-commerce</span>
                    <span class="work-name">Nova Aura — Магазин косметики</span>
                    <p class="work-desc">Мінімалістичний дизайн з акцентом на типографіку та чисті продуктові картки.</p>
                </div>

                <div class="work-card" style="animation-delay: 0.5s;">
                    <span class="work-tag">Fintech</span>
                    <span class="work-name">ZenithPay — Мобільний банк</span>
                    <p class="work-desc">Інтерфейс додатку з темною темою та футуристичними графіками витрат.</p>
                </div>

                <div class="work-card" style="animation-delay: 0.6s;">
                    <span class="work-tag">Portfolio</span>
                    <span class="work-name">Architectural Studio "Vertical"</span>
                    <p class="work-desc">Преміальний лендинг для архітектурного бюро з ефектом паралаксу.</p>
                </div>
            </div>

            <span class="section-title">Послуги</span>
            <div class="price-list">
                <div class="price-item"><span>Landing Page</span><strong>від $200</strong></div>
                <div class="price-item"><span>Інтернет-магазин</span><strong>від $500</strong></div>
                <div class="price-item"><span>UI/UX аудит</span><strong>від $100</strong></div>
            </div>
        </div>
    </body>
    </html>
    """

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
