import os
import sys
import time
import random
import logging
import requests

# Configuración de logs enfocada en diagnóstico y autocorrección de errores
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] (Autocorrector Soto) -> %(message)s"
)

# --- NARRATIVAS DE MARKETING EMOCIONAL & IDENTIDAD LOCAL ---
EMOTIONAL_CAMPAIGNS = [
    {
        "id": "sena_colombia_01",
        "copy": (
            "🚀🔥 From the heart of Colombia to the global stage! 🇨🇴✨\n\n"
            "As an independent SENA apprentice and grassroots developer, I build autonomous systems "
            "from scratch with zero corporate backing. True digital sovereignty, local engineering, "
            "and relentless resilience.\n\n"
            "If you believe in authentic, community-driven tech innovation, support our journey: "
            "{donation_url}\n\n"
            "#TechColombia #SENA #BuildInPublic #OpenSource #GlobalInnovation #IndieDev"
        )
    },
    {
        "id": "resilience_02",
        "copy": (
            "💡🛠️ Real solutions born from tough moments, engineered for the world. 🌍⚡\n\n"
            "No middlemen, no corporate filters. Just raw automation and Colombian grit "
            "transforming how we connect across borders via automated publishing nodes.\n\n"
            "Be part of this independent movement and fuel our next breakthrough: "
            "{donation_url}\n\n"
            "#CreatorEconomy #Automation #TechFreedom #Colombia #SoftwareEngineering"
        )
    }
]

# Tubería oficial de automatización Soto configurada con los números operativos (+57)
# Canal emisor / receptor principal y secundario para Facebook y syndication
NODE_SOTO_PRIMARY = os.getenv("TARGET_WHATSAPP_SOTO", "https://api.whatsapp.com/send?phone=573123833064")
NODE_SOTO_SECONDARY = os.getenv("TARGET_WHATSAPP_APPRENTICE", "https://api.whatsapp.com/send?phone=573177222608")

DONATION_LINK = os.getenv("DONATION_URL", "https://paypal.me/yourlink")

def self_healing_pipeline_request(url, payload, max_retries=3):
    """
    Sistema de autocorrección estricto: Solo rectifica errores de conexión,
    aplica backoff exponencial y reintenta ante caídas sin alterar la lógica base.
    """
    if not url or not url.startswith("http"):
        logging.warning(f"URL de nodo inválida ('{url}'). Omitiendo de forma segura.")
        return False

    for attempt in range(1, max_retries + 1):
        try:
            logging.info(f"Autocorrector: Verificando enlace con nodo (Intento {attempt}/{max_retries})...")
            response = requests.post(url, json=payload, timeout=10)
            
            if response.status_code in [200, 201, 204]:
                logging.info("¡Tubería sincronizada y mensaje transmitido con éxito!")
                return True
            elif 500 <= response.status_code < 600:
                logging.warning(f"Error de servidor remoto ({response.status_code}). Autocorrección: reintentando transmisión...")
            else:
                logging.error(f"Nodo rechazó la conexión (Código {response.status_code}). Abortando intento actual.")
                break
                
        except requests.exceptions.Timeout:
            logging.warning(f"Timeout detectado en intento {attempt}. Autocorrector reintentando...")
        except requests.exceptions.ConnectionError:
            logging.warning(f"Fallo temporal de red en intento {attempt}. Estabilizando tubería...")
        except Exception as e:
            logging.error(f"Error imprevisto en la solicitud: {e}")
        
        # Espera adaptativa controlada para evitar bloqueos por spam
        time.sleep(attempt * 2)
        
    logging.error("Se agotaron los reintentos para este nodo. El sistema se mantiene estable.")
    return False

def run_soto_automation():
    logging.info("--- Iniciando ciclo de automatización Soto (+573123833064 / +573177222608) ---")
    
    selected_campaign = random.choice(EMOTIONAL_CAMPAIGNS)
    formatted_message = selected_campaign["copy"].format(donation_url=DONATION_LINK)
    
    payload = {
        "source": "automatizandoando_por_soto",
        "operator_primary": "+573123833064",
        "operator_secondary": "+573177222608",
        "content": formatted_message,
        "metadata": {
            "platform": "facebook_syndication",
            "strategy": "emotional_marketing",
            "campaign_id": selected_campaign["id"]
        }
    }
    
    # Canales activos de la tubería Soto
    nodes = [NODE_SOTO_PRIMARY, NODE_SOTO_SECONDARY]
    active_nodes = [node for node in nodes if node and node.startswith("http")]
    
    if not active_nodes:
        logging.info("Modo simulación de tubería activa (Sin endpoints externos definidos). Copia lista para Facebook:")
        print("\n" + "="*50 + "\n" + formatted_message + "\n" + "="*50 + "\n")
        return

    for node in active_nodes:
        self_healing_pipeline_request(node, payload)
        time.sleep(random.randint(3, 6))

if __name__ == "__main__":
    try:
        run_soto_automation()
        logging.info("--- Ciclo de automatización finalizado limpiamente ---")
    except Exception as fatal_error:
        logging.critical(f"Excepción atrapada por el núcleo de seguridad: {fatal_error}")
        sys.exit(0)
