import lularize

source = "/Users/christopherbroski/Desktop/lularize/"
watermark = "LuLaRoe Stacy Leasure-Broski"

print 'Left-to-right position of the closeup (0 - 100) or hit enter for 50'
left_pos = raw_input('> ')

if left_pos == '':
    left_pos = 50

print 'Top-to-bottom position of the closeup (0 - 100) or hit enter for 50'
top_pos = raw_input('> ')

if top_pos == '':
    top_pos = 50

detail = [int(left_pos), int(top_pos)]

lularize.processFolder(source, watermark, (246, 117, 153), detail, False, True)
