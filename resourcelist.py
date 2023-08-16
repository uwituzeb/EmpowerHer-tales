def display_resources():
    resources = [
            {
                "title": "Women Creating Wealth",
                "description": "A book by the Graca Machel Trust that tells the stories of African women entrepreneurs",
                "link": "https://mastercardfdn.org/report/women-creating-wealth-wcw-a-collection-of-stories-by-african-women-entrepreneurs/"
            },
            {
                "title": "Inua Dada Foundation",
                "description": "A movement founded by Janet Mbugua that aims to end period poverty and uphold the dignity and rights of every girl.",
                "link": "https://inuadadafoundation.org/"
            },
            {
                "title" : "Women of Impact",
                "description": "A compendium by the AU that aims to recognise and celebrate African women and girls making a difference through their impactful leadership.",
                "link": "https://au.int/en/documents/20230801/women-impact-inspiring-stories-african-women-leaders"
            },
            {
                "title" : "Women in Tech Africa",
                "description" : "Supporting Women in Tech Across Africa(WITA) to Positively to Impact their Communities Positively.",
                "link" : "http://www.womenintechafrica.com/"
            }
        ]

    for resource in resources:
        print(f'Title: {resource["title"]}')
        print(f'Description: {resource["description"]}')
        print(f'Link: {resource["link"]}')
        print('---------------------------')


display_resources()
