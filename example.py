from obd2 import OBD2


ELM327_ADDRESS = "XX:XX:XX:XX:XX:XX"


def main():
    obd = OBD2(ELM327_ADDRESS)

    print("Conectando al ELM327...")

    try:
        obd.connect()
        print("Conectado.")

        print("Enviando ATZ...")
        obd.send("ATZ")

        response = obd.receive()

        print("Respuesta del ELM327:")
        print(response)

    except Exception as error:
        print(f"Error: {error}")

    finally:
        obd.close()


if __name__ == "__main__":
    main()