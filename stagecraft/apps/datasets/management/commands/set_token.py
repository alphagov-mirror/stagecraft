from django.core.management.base import BaseCommand, CommandError

from stagecraft.libs.mass_update import DataSetMassUpdate


class Command(BaseCommand):
    help = ("Updates the DataSets matched by the DataType "
            "name (data-type-name), DataGroup name "
            "(date-group-name) or combination thereof with the "
            "specified bearer_token")

    def add_arguments(self, parser):
        parser.add_argument("args", nargs='+')
        parser.add_argument(
            '--data-type-name',
            dest='data_type',
            help=("Specify the data type name to match against when updating datasets")
        )
        parser.add_argument(
            '--data-group-name',
            dest='data_group',
            help=("Specify the data group name to match against when updating datasets")
        )

    def handle(self, *args, **options):
        if not len(args):
            raise CommandError("No new bearer_token given, see --help")
        elif not len(args) == 1:
            raise CommandError("Please provide a single bearer_token only, see --help")

        updated = DataSetMassUpdate \
            .update_bearer_token_for_data_type_or_group_name(
            self._build_query(options), args[0])
        self.stdout.write("Updated {} records".format(updated))

    def _build_query(self, options):
        query = {}
        for k, v in options.iteritems():
            if k in ["data_type", "data_group"] and v:
                query[k] = v

        if not len(query):
            raise CommandError(
                "Please provide a data_type or data_group"
                "name to match against, see --help")

        return query
