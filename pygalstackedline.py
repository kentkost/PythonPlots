import pygal

#https://github.com/Kozea/pygal/issues/449
class _PygalStackedLineWithLimit(pygal.StackedLine):
    """
    Fork of pygal.StackedLine that adds (rather hacky) support for adding
    limit lines like ``.add('limit', [..values..], fill=False, stack=False)``
    """

    def __init__(self, *args, **kvargs):
        super().__init__(*args, **kvargs)
        self.__index_to_stack_flag = []

    def add(self, *args, **kvargs):
        stack = kvargs.pop('stack', True)
        self.__index_to_stack_flag.append(stack)
        return super().add(*args, **kvargs)

    def _points(self, x_pos):
        zipped_backup = list(zip(self.series, self.__index_to_stack_flag))
        series_to_stack = [serie for serie, stack in zipped_backup if stack]
        series_not_to_stack = [serie for serie, stack in zipped_backup
                               if not stack]

        self.series = series_to_stack
        super()._points(x_pos)

        self.series = series_not_to_stack
        super(pygal.StackedLine, self)._points(x_pos)

        # Restore
        self.series = [serie for serie, _ in zipped_backup]


if __name__ == '__main__':
    chart = _PygalStackedLineWithLimit(x_label_rotation=25, show_dots=False,
                                       fill=True)

    chart.title = 'StackedLine + limit lines'
    chart.x_labels = ['Jan', 'Feb', 'Mar']

    chart.add('A', [1, 1.2, 1.6, 2])
    chart.add('B', [1.6, 1.6, 1.7, 1.6])
    chart.add('C', [2, 3, 2, 1.5])

    chart.add('Limit 1', [4, 4, 4, 4], fill=False, stack=False)
    chart.add('Limit 2', [3, 3, 3, 3], fill=False, stack=False)

    chart.render_to_file('pygalstackedlinesample.html')