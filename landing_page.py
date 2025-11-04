LANDING_PAGE_HTML = b"""
<!DOCTYPE html>
<html lang='en'>
<head>
    <meta charset='UTF-8'>
    <meta name='viewport' content='width=device-width, initial-scale=1.0'>
    <title>Colours API 🚀</title>
    <link href='https://fonts.googleapis.com/css2?family=Montserrat:wght@700&family=Roboto:wght@400&display=swap' rel='stylesheet'>
    <style>
        body {
            font-family: 'Montserrat', 'Roboto', sans-serif;
            background: linear-gradient(135deg, #ff6ec4 0%, #7873f5 100%);
            color: #222;
            margin: 0;
            padding: 0;
            min-height: 100vh;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: flex-start;
        }
        .container {
            background: rgba(255,255,255,0.85);
            border-radius: 24px;
            box-shadow: 0 8px 32px rgba(120,115,245,0.15);
            padding: 2.5rem 2rem 2rem 2rem;
            margin-top: 3rem;
            max-width: 480px;
            width: 100%;
            text-align: center;
        }
        h1 {
            font-size: 2.5rem;
            margin-bottom: 0.5rem;
            letter-spacing: -2px;
            color: #ff6ec4;
        }
        .subtitle {
            font-size: 1.2rem;
            margin-bottom: 1.5rem;
            color: #7873f5;
        }
        .example-link {
            display: inline-block;
            margin: 1.5rem 0;
            padding: 0.75rem 1.5rem;
            background: linear-gradient(90deg, #ff6ec4 0%, #7873f5 100%);
            color: #fff;
            border-radius: 999px;
            font-weight: bold;
            text-decoration: none;
            font-size: 1.1rem;
            box-shadow: 0 2px 8px rgba(120,115,245,0.12);
            transition: transform 0.1s;
        }
        .example-link:hover {
            transform: scale(1.07);
        }
        .customers {
            margin-top: 2.5rem;
            text-align: center;
        }
        .badges {
            display: flex;
            flex-wrap: wrap;
            gap: 1rem;
            justify-content: center;
            margin-top: 1rem;
        }
        .badge {
            background: #fff;
            border-radius: 16px;
            box-shadow: 0 2px 8px rgba(120,115,245,0.10);
            padding: 0.7rem 1.2rem;
            font-size: 1rem;
            font-weight: 600;
            color: #7873f5;
            display: flex;
            align-items: center;
            gap: 0.5rem;
        }
        .badge-emoji {
            font-size: 1.3rem;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>Colours API 🌈</h1>
        <div class="subtitle">Gen-Z's favourite way to generate colour palettes & images. <span style="font-size:1.5rem;">✨</span></div>
        <p>Just add hex codes to the URL to create a palette image.<br>
        Example: <code>/red-orange-purple</code></p>
        <a class="example-link" href="/random-random-random">Try Example &rarr;</a>
        <div class="customers">
            <div style="font-size:1.1rem; color:#222; margin-bottom:0.5rem;">Trusted by the coolest startups:</div>
            <div class="badges">
                <div class="badge"><span class="badge-emoji">🦄</span>Unicornify</div>
                <div class="badge"><span class="badge-emoji">📱</span>Snapster</div>
                <div class="badge"><span class="badge-emoji">🎨</span>PalettePal</div>
                <div class="badge"><span class="badge-emoji">🤖</span>Botify</div>
                <div class="badge"><span class="badge-emoji">🔥</span>LitPics</div>
                <div class="badge"><span class="badge-emoji">🛹</span>Sk8r</div>
                <div class="badge"><span class="badge-emoji">🌟</span>Starlite</div>
                <div class="badge"><span class="badge-emoji">🍕</span>SliceTech</div>
            </div>
        </div>
    </div>
</body>
</html>
"""
