# Batalha Naval

## Sobre o Projeto

Este projeto foi desenvolvido como exercício prático para ensinar conceitos de **Programação Orientada a Objetos (OOP)** na disciplina de Lógica de Programação, durante o 3º semestre do curso de Análise e Desenvolvimento de Sistemas. O objetivo é proporcionar uma experiência de aprendizado sobre organização de código, encapsulamento, reutilização e separação de responsabilidades em um jogo clássico.

---

## Regras de Negócio

- O jogo é disputado entre dois jogadores: um humano e o computador.
- Cada jogador possui um campo de batalha (10x10) onde suas embarcações são posicionadas aleatoriamente.
- As embarcações disponíveis são: Porta-Aviões, Encouraçado, Cruzador e Submarino, cada uma com tamanho e símbolo próprios.
- Os jogadores se alternam em turnos, escolhendo uma posição (linha e coluna) para atacar no campo adversário.
- O tiro pode resultar em:
  - **Acerto na água**: marcação com `*` no campo.
  - **Acerto em embarcação**: marcação com `X` e informação de qual embarcação foi atingida.
- O jogo termina quando todas as embarcações de um dos jogadores são destruídas, declarando o outro como vencedor.

---

## Como rodar o projeto localmente

1. **Pré-requisitos:**  
   - Python 3.10 ou superior instalado.

2. **Clone o repositório:**
   ```bash
   git clone git@github.com:RaulRory/batalha-naval.git
   cd batalha-naval
   ```

3. **Execute o jogo:**
   ```bash
   python -m src.main
   ```

---

## Estrutura de Pastas do Projeto

```
Batalha Naval/
├── src/
│   ├── battlefield/
│   │   └── battlefield.py
│   ├── players/
│   │   └── players.py
│   ├── shoots/
│   │   └── shoot.py
│   ├── vessels/
│   │   └── vessel.py
│   └── main.py
├── README.md
```

---

## O que o projeto utiliza

- **Python 3.10+**
- Programação Orientada a Objetos (OOP)
- Tipagem estática com `typing`
- Estrutura modularizada por responsabilidade (battlefield, players, shoots, vessels)

---


## Resumo do Fluxo do Jogo

- O arquivo `main.py` inicia o jogo, cria os campos de batalha e posiciona os navios.
- Jogador humano e computador se alternam em turnos, realizando disparos.
- O campo de batalha processa cada tiro, informando se foi acerto ou erro.
- O jogo termina quando todas as embarcações de um dos jogadores são destruídas.

---

## Dúvidas

Para dúvidas ou sugestões, abra uma issue no repositório.
