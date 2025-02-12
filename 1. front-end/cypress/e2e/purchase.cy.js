/// <reference types="cypress"/>
import { texts } from '../support/strings'

describe('Cenário de Testes para o site Amazon', () => {
  beforeEach(() => {
    // Hook
    cy.log('1 - acessa pagina inicial')
    cy.visit('/')
  })

  // Casos de teste
  it('Deve buscar por produto relacionado à IA', () => {
    cy.log('2 - preenche o campo de busca')
    cy.search_bar(texts.bar)
  })

  it('Deve verificar detalhes do produto buscado para adiciona-lo ao carrinho', () => {
    cy.log('3 - adiciona livro')
    cy.add_to_car()
  })
})