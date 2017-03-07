from django.contrib.syndication.views import Feed

from models import Artigo


class UltimosArtigos(Feed):
    title = 'Ultimos artigos do blog ProjetoDjango.'
    link = '/'

    def items(self):
        print '-------------------------'
        print'passou aqui'
        return Artigo.objects.all()

    def item_title(self, artigo):
      return artigo.titulo
		
    def item_description(self, artigo):
      return artigo.conteudo

    def item_link(self, artigo):
        print '-------------------------'
        print'passou aqui 2'
        return 'artigo/%d/'%artigo.id

    # def items(self):
    #     return NewsItem.objects.order_by('-pub_date')[:5]
    
    # def item_link(self, item):
    #     return reverse('news-item', args=[item.pk])