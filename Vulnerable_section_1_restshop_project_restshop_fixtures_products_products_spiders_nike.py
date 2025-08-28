                                           callback=self.parse_item,
                                           meta={'tags': response.meta['tags']})
             else:
                yield response.follow(item.css('.grid-item-image-wrapper a'),
                                       callback=self.parse_item,
                                       meta={'tags': response.meta['tags']})
 
             sizes = [size.strip() for size in sizes]
 
         yield {
             'title': title,
             'price': price,
             'sizes': sizes,