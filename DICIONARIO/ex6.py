dicionario_aninhado = {
  "cliente": {
      "nome": "Alice",
      "idade": 30
  },
  "compra": {
      "produto": "Livro",
      "preço": 25.50
  }
}

nome_cliente = dicionario_aninhado["cliente"]["nome"]
produto_comprado = dicionario_aninhado["compra"]["produto"]
print(nome_cliente)  # Saída: Alice
print(produto_comprado)  # Saída: Livro
