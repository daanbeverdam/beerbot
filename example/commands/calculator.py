from pybot.command import Command


class CalculatorCommand(Command):

    def reply(self):
        if self.is_active():
            return self.collect_input()
        else:
            return self.start()

    def start(self):
        prompt = self.dialogs['prompt']
        calculator = ([['1', '2', '3', '+'], ['4', '5', '6', '-'],
                      ['7', '8', '9', '*'], ['0', '.', '=', '/']])
        self.data['calc_starter'] = self.message.sender_id
        self.data['calc_query'] = ''
        self.data['calculator_active'] = True
        return {'message': prompt, 'keyboard': calculator, 'one_time': False,
                'selective': True, 'message_id': self.message.id,
                'force_reply': True}

    def collect_input(self):
        operators = ['*', '/', '.', '+', '-']
        if self.message.sender_id == self.data['calc_starter']:
            if self.message.text.isdigit() or self.message.text in operators:
                query = self.data['calc_query']
                query += self.message.text
                self.data['calc_query'] = query
                return {'message': None}
            elif self.message.text == '=':
                return self.answer()
        return {'message': None}

    def answer(self):
        self.stop()
        try:
            answer = str(eval(self.data['calc_query']))
            return {'message': answer, 'keyboard': None}
        except:
            return {'message': self.dialogs['error'], 'keyboard': None}

    def stop(self):
        self.data['calculator_active'] = False
