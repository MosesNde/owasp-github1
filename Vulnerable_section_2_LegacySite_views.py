         # KG: Where is this data coming from? RAW SQL usage with unkown
         # KG: data seems dangerous.
         print(card_data.strip())
        signature = json.loads(card_data)['records'][0]['signature']
         # signatures should be pretty unique, right?
         card_query = Card.objects.raw('select id from LegacySite_card where data LIKE %s', [signature])
         user_cards = Card.objects.raw('select id, count(*) as count from LegacySite_card where LegacySite_card.user_id = %s' % str(request.user.id))