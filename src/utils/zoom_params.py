class ZoomParams:

    def __init__(self, zoom_level=1.0, base_cell_size_ratio=0.008,
                 base_sampling_ratio=0.02, min_zoom=0.1, max_zoom=10.0):
        self.zoom_level = max(min_zoom, min(max_zoom, zoom_level))
        self.base_cell_size_ratio = base_cell_size_ratio
        self.base_sampling_ratio = base_sampling_ratio
        self.min_zoom = min_zoom
        self.max_zoom = max_zoom

    def get_cell_size(self, width, height, proportionally=True):
        if proportionally:
            avg_dimension = (width + height) / 2
            base_size = avg_dimension * self.base_cell_size_ratio
        else:
            base_size = 4

        return base_size * self.zoom_level

    def get_sampling_distance(self, width, height):
        ''
        avg_dimension = (width + height) / 2
        base_distance = avg_dimension * self.base_sampling_ratio

        return base_distance / self.zoom_level

    def get_irregularity_factor(self):
        """Dostosowuje nieregularność w zależności od zoom"""
        # Przy dużym zoom więcej detali, przy małym mniej
        base_irregularity = 0.3
        return base_irregularity * min(1.0, self.zoom_level)