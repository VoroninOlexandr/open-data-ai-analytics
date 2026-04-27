# Open Data AI Analytics - Infrastructure

Цей проект містить конфігурацію Terraform для автоматичного розгортання інфраструктури в Azure.

## Склад інфраструктури:
* **VM:** Standard_D2s_v3 (Ubuntu 22.04)
* **Регіон:** North Europe
* **Автоматизація:** Docker & Docker Compose встановлюються автоматично через cloud-init.

## Як запустити:
1. `terraform init`
2. `terraform apply -auto-approve`

## Результат:
Веб-інтерфейс доступний за адресою `http://40.112.90.119:5000`
