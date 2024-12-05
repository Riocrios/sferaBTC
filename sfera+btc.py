import os
import ecdsa
import hashlib
import base58
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import time

# Кількість точок (адрес)
num_points = 500  # Можна збільшити після тестування

# Функція генерації біткоїн-адреси
def generate_bitcoin_address():
    private_key = os.urandom(32)
    sk = ecdsa.SigningKey.from_string(private_key, curve=ecdsa.SECP256k1)
    vk = sk.verifying_key
    public_key = b'\x04' + vk.to_string()

    # Створення хешу публічного ключа (SHA-256 та RIPEMD-160)
    sha256_bpk = hashlib.sha256(public_key).digest()
    ripemd160_bpk = hashlib.new('ripemd160', sha256_bpk).digest()
    hashed_public_key = b'\x00' + ripemd160_bpk

    # Генерація контрольної суми
    checksum = hashlib.sha256(hashlib.sha256(hashed_public_key).digest()).digest()[:4]

    # Створення біткоїн-адреси
    address = base58.b58encode(hashed_public_key + checksum)
    return private_key.hex(), address.decode(), hashlib.sha256(private_key).hexdigest()

# Генерація адрес для точок
addresses = [generate_bitcoin_address() for _ in range(num_points)]

# Золотий кут
phi = np.pi * (3. - np.sqrt(5.))

# Координати точок
y = 1 - (np.arange(num_points) / float(num_points - 1)) * 2
radius = np.sqrt(1 - y * y)
theta = phi * np.arange(num_points)

x = np.cos(theta) * radius
z = np.sin(theta) * radius

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Нанесення точок
sc = ax.scatter(x, y, z, s=1)

# Таймер для обмеження частоти виклику
last_update_time = 0
update_interval = 0.1  # 100 мс

# Функція відображення адрес при наведенні
def on_move(event):
    global last_update_time
    current_time = time.time()
    if current_time - last_update_time < update_interval:
        return  # Ігнорувати виклик, якщо інтервал не минув

    last_update_time = current_time
    if sc.contains(event)[0]:
        ind = sc.contains(event)[1]['ind'][0]
        private_key, address, sha256_hash = addresses[ind]
        print(f"Індекс: {ind}")
        print(f"Приватний ключ: {private_key}")
        print(f"Біткоїн-адреса: {address}")
        print(f"SHA-256 хеш: {sha256_hash}")

fig.canvas.mpl_connect('motion_notify_event', on_move)

plt.show()
