                         datetime: '2016-10-14 08:00:00+00:00',
                         timezone: 'Atlantic/Azores'
                     };
                    expect(DateUtils.localize(context)).toEqual('Oct 14, 2016 08:00 AZOST');
                 });
 
                 it('generates a more complex localized datetime string', function() {