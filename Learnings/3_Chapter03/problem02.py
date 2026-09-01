#letter fill

letter ='''Dear <|Name|>,
            you are selected!
            <|Date|>'''
print(letter.replace("<|Name|>", "Parikshit").replace("<|Date|>", "16 November 2050"))