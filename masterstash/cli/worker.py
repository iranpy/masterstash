from masterstash.cli.base import Cli
from masterstash.settings import settings
from masterstash.rabbitmq import ConsumerMApper
from masterstash.order.finalized_order import FinalizedOrderConsumer

class Worker(Cli):
    def add_commands(self, parser):
        parser.add_argument('-a', '--action', type=str)
        parser.add_argument('-m', '--model', type=str)
        parser.add_argument('-l', '--loglevel', type=str)
        # parser.add_argument('-s', '--store_location', type=str)

    def run(self, **kwargs):
        model = kwargs.get('model')
        consumer = getattr(ConsumerMApper, model)
        worker = consumer(**settings.WORKERS[model])
        worker.run()

def main():
    Worker().execute_cli()

if __name__ == '__main__':      # pragma: no cover
    main()
