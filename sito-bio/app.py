from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    dati = {
        'nome': 'Awsaf Æ7',
        'descrizione': 'Editor & Website builder | Join my discord if you want free overlays, comps, presets and for other things!!',
        
        # Link social reali per i pulsanti rotondi/colorati
        'link_discord': 'https://discord.gg/9ADy3MVzZ',
        'link_tiktok': 'https://www.tiktok.com/@awsaf.ae?is_from_webapp=1&sender_device=pc',
        'link_youtube': 'https://youtube.com/@awsaf_editz?si=lJ0E4e0eEfLj2CYl',
        
        # Link reali per i tre grandi rettangoli con i bordi rossi
        'link_workflow': 'https://workflowenhancer.com',
        'link_downgrade': 'https://aedowngradefiles.com',
        'link_wtm_tiktok': 'https://chromewebstore.google.com/detail/wtm-tiktok-method/bfheeapgnbphifakecnklmdampcppffh'
    }
    return render_template('index.html', utente=dati)

if __name__ == '__main__':
    app.run(debug=True)
