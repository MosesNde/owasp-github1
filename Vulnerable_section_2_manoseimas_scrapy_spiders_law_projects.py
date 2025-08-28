     )
 
     rules = [
        Rule(mp_projects_link_extractor, 'parse_mp_project_index'),
     ]
 
     pipelines = (
         loader.add_value('project_number', self._extract_proposal_no(xs))
         loader.add_value('source', self._get_source(response.url, 'p_asm_id'))
         loader.add_value('project_number', self._extract_proposal_no(xs))
        yield loader
         passed_xs = xs.xpath('td[4]/a')
         if passed_xs:
            loader = Loader(self, item=PassedLawProjectProposer(),
                             selector=passed_xs, response=response)
             doc_id = self._get_query_attr(
                 passed_xs.xpath('@href').extract()[0], 'p_id'
             )
            loader.add_value('id', doc_id)
             doc_number = self._extract_passed_no(passed_xs)
            loader.add_value('passing_number', doc_number)
            loader.add_xpath('passing_url', '@href')
            loader.add_value('date', proposal_date)
            loader.add_value('source', self._get_source(response.url,
                                                         'p_asm_id'))
            yield loader
 
     def parse_mp_project_index(self, response):
         sel = Selector(response)