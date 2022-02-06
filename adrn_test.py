import serial
import time

while True:

    try:
        ser = serial.Serial(port="COM"+f"{int(input('Введите номер COM порта: '))}",
                            baudrate=9600,
                            parity=serial.PARITY_NONE,
                            stopbits=serial.STOPBITS_ONE,
                            bytesize=serial.EIGHTBITS,
                            timeout=1, xonxoff=0, rtscts=0)
        time.sleep(1)
    except:
        print('Соединение не установлено. Проверьте наличие и'
              ' номер COM порта')
        input('Нажмите Enter для повторного выбора COM порта. ')
        continue

    else:
        if ser.is_open:
            print(f'Соединение c {ser.port} установлено.\nВыберите операцию: '
                  '0 - Выключить; '
                  '1 - Синий; '
                  '2 - Зеленый; '
                  '3 - Красный; '
                  '4 - Белый; '
                  'х - Выход')

            while True:
                data = input('Введите номер команды: ')
                if data == '1':
                    ser.write(b'000000255')
                elif data == '2':
                    ser.write(b'000255000')
                elif data == '3':
                    ser.write(b'255000000')
                elif data == '4':
                    ser.write(b'255255255')
                elif data == '0':
                    ser.write(b'000000000')
                elif data == 'x':
                    ser.write(b'000000000')
                    ser.close()
                    break

        if ser.is_open is False:
            break
