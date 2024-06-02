def ip_to_decimal(binary_ip):
  octets = binary_ip.split('.')
  decimal_ip = []
  for octet in octets:
    decimal_ip.append(str(int(octet, 2)))
  return '.'.join(decimal_ip)

def decimal_to_binary(decimal_ip):
  octets = decimal_ip.split('.')
  binary_ip = []
  for octet in octets:
    binary_ip.append(bin(int(octet))[2:].zfill(8))
  return '.'.join(binary_ip)

while True:
  # Запрос типа преобразования
  conversion_type = input("Введите '210' для 2 в 10- или '102' для 10 в 2: ")
  if conversion_type not in ["210", "102"]:
    print("Неверный тип преобразования. Повторите попытку.")
    continue

  # Запрос IP-адреса
  ip_address = input("Введите IP-адрес: ")

  # Преобразование IP-адреса
  if conversion_type == "210":
    result = ip_to_decimal(ip_address)
  else:
    result = decimal_to_binary(ip_address)

  # Отображение результата
  print(f"Преобразованный IP-адрес: {result}")
