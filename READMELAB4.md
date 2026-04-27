Open Data AI Analytics - Infrastructure

Цей репозиторій містить конфігурацію Terraform для автоматичного розгортання хмарної інфраструктури в Azure.

## Склад системи
* **VM:** Standard_D2s_v3 (Ubuntu 22.04 LTS)
* **Регіон:** North Europe (northeurope)
* **Автоматизація:** Docker та Docker Compose встановлюються автоматично через скрипт `cloud-init`.
* **Додаток:** Веб-інтерфейс аналітики на порту 5000.

---

Інструкція з використання


Як виконати розгортання (Terraform Apply)
Перейдіть у папку з проєктом та запустіть процес створення інфраструктури:

```bash
# Ініціалізація Terraform
terraform init

# Створення ресурсів
terraform apply -auto-approve


 Як перевірити результат
Після успішного завершення команди Terraform виведе у консоль вашу публічну IP-адресу (public_ip_address).

Скопіюйте цю IP-адресу.

Відкрийте браузер і введіть: http://40.112.90.119:5000/

Як виконати видалення

terraform destroy -auto-approve
