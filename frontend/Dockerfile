# frontend/Dockerfile

# Використовуємо Node.js для розробки
FROM node:20-alpine

WORKDIR /app

# Копіюємо package.json
COPY package.json package-lock.json ./

# Встановлюємо залежності
RUN npm install

# Копіюємо весь код
COPY . .

# Відкриваємо порт Vite (за замовчуванням 5173)
EXPOSE 5173

# Запускаємо в режимі розробки з хостом 0.0.0.0 (щоб було видно ззовні контейнера)
CMD ["npm", "run", "dev", "--", "--host"]