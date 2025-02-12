// Importa arquivo para constantes
import { texts } from './strings'

const book = texts.bar
const book_status = texts.condition

// Metodo para realizar busca do livro
Cypress.Commands.add('search_bar', (text) => {
  cy.get('#twotabsearchtextbox').type(text)
  cy.get('#nav-search-submit-button').click()
})
// Metodo para adicionar livro ao carrinho
Cypress.Commands.add('add_to_car', () => {
  cy.search_bar(texts.bar)
  // Valida livro buscado e seleciona-o
  cy.get('div[data-index="2"]').should('be.visible')
  cy.get(`h2[aria-label="${book}"`).click()
  
  cy.log('3 - a.i) verifica edicao')
  cy.get('#bylineInfo').contains('Edição Inglês')

  cy.log('3 - a.ii) verifica autor')
  cy.get('.a-link-normal').contains('Chip Huyen')
  
  cy.log('3 - a.iii) verifica se esta comprando livro fisico')
  cy.get('#tmm-grid-swatch-PAPERBACK').click()
  cy.get('#tmm-grid-swatch-PAPERBACK').
    should('have.attr', 'class',
    'a-column a-span12 a-text-left swatchElement selected celwidget')

  cy.log('3 - a.iv) verifica condicao nova selecionada')
  cy.get('#morpheus-sidesheet-ingress').click()
  cy.get("#morpheusAodEntryLink_1098166302_new").click()
  cy.get('#aod-offer-heading').contains(`${book_status}`)
  
  cy.get('#aod-close').click()
  cy.get('#add-to-cart-button').click()
  cy.log('4 - valida mensagem de adicao')
  cy.contains('Adicionado ao carrinho').should('be.visible')
  // Documentacao
  cy.log('5 - presente na pasta "five"')
})
