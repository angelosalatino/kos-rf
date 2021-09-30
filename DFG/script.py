with open('./dfg.html') as html_file:
    n_first_second_level = 18
    n_substring = html_file.read().count('review_boards/list/index.jsp?id=')
    total = n_first_second_level + n_substring

    print('The number of first and second level disciplines are 18 (manually counted from https://www.dfg.de/download/pdf/dfg_im_profil/gremien/fachkollegien/amtsperiode_2020_2024/fachsystematik_2020-2024_en_grafik.pdf')
    print('The number of substrings matching \'review_boards/list/index.jsp?id=\' which identifies a linkable topic review board are %s' % n_substring)
    print('Total subjects in DFG %s' % total)