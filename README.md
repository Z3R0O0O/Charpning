# Challenge Pride Security 2023

## Defesa Cibernética
<br>
<p align="center">
<img src="https://github.com/Z3R0O0O/Challenge/blob/main/CHARP_Logo-White.png">
</p>
<br>

### Integrantes do grupo CHARP:
+ Danilo da Gama Campos
+ Eduardo do Nascimento Silva
+ Gustavo Duarte Bezerra da Silva
+ Henrique Batista de Souza

### Sobre:
O Charpning é um código em python que limita os processos que podem ser executados no sistema, ou seja, caso o processo que está sendo iniciado não possuir seu nomme da lista de exceções, o processo é encerrado!
Para encerrar ou não o processo ele leva em conta dois paramêtros, se consome mais de 23% da CPU (Consumo médio do Ransomware open source escolhido para análise) e se está na lista, caso nenhum desses paramêtros sejam compaátiveis, ele é encerrado!

### Instalação
pip install psutil\n
git clone https://github.com/Z3R0O0O/Charpning\n
cd Charpning

### Ransomware utilizado para testes:
https://github.com/tarcisio-marinho/GonnaCry/

### Especificações da VM de teste:
+ RAM: 4GB
+ Processadores: 4
+ Memória: 20GB
+ Sistema Operacional: Ubuntu 22.04.3
