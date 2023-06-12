import webapp2

class EvenNumbersHandler(webapp2.RequestHandler):
    def get(self):
        n = self.request.get('n')
        if not n.isdigit():
            self.response.write("Invalid input. Please provide a valid number.")
            return
        
        n = int(n)
        even_numbers = [str(i) for i in range(2, 2*n+1, 2)]
        self.response.write("Even Numbers: {}".format(', '.join(even_numbers)))

app = webapp2.WSGIApplication([
    ('/even_numbers', EvenNumbersHandler),
], debug=True)
