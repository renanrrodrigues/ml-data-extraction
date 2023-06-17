'''
LINK PARA PESQUISA DE PLACAS MÃE NO MERCADO LIVRE (LINK COMPLETO COM FILTROS)
https://lista.mercadolivre.com.br/informatica/componentes-pc/placas/placas-mae/
kit-i5
_Frete_Full_NoIndex_True#applied_filter_id%3Dshipping_highlighted_fulfillment%26applied_filter_name
%3DTipo+de+envio%26applied_filter_order%3D2%26applied_value_id%3Dfulfillment%26applied_value_name
%3DFull%26applied_value_order%3D1%26applied_value_results%3D52%26is_custom%3Dfalse

Link somente com o filtro de fullfilment:
Filtro fullfilment: https://lista.mercadolivre.com.br/informatica/componentes-pc/placas/placas-mae/kit-i5_Frete_Full_NoIndex_True

filtro para pegar somente fullfilment: (Frete_Full_NoIndex_True)

montando um link

LINK_BASE = 'https://lista.mercadolivre.com.br/'

CATEGORIA = 'informatica/componentes-pc/placas/placas-mae/'

NOME_PRODUTO = 'kit-i5' # usamaos _ para separar as palavras

FILTRO_FULLFILMENT = '_Frete_Full_NoIndex_True'

'''

from time import sleep

from model.driver_edge import DriverEdge

LINK_BASE = 'https://lista.mercadolivre.com.br/'
CATEGORIA = 'informatica/componentes-pc/placas/placas-mae/'
FILTRO_FULLFILMENT = '_Frete_Full_NoIndex_True'



def test_headless(driver, product_name=None):
    driver.get(f'{LINK_BASE}{CATEGORIA}{product_name}{FILTRO_FULLFILMENT}')

    chk_existe_paginacao = driver.execute_script("return document.getElementsByClassName('andes-pagination__button--next').length")
    while chk_existe_paginacao > 0:
        driver.execute_script("document.getElementsByClassName('andes-pagination__button--next')[0].getElementsByClassName('ui-search-link')[0].click()")
        print('clicou')
        sleep(4)
        chk_existe_paginacao = driver.execute_script("return document.getElementsByClassName('andes-pagination__button--next').length")
    print('fim')
    sleep(5)
    driver.quit()





if __name__ == '__main__':
    driver = DriverEdge().get_driver() # objeto driver

    test_headless(driver, 'kit-placa-mae')
