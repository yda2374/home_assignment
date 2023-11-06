import numpy as np
import pandas as pd

class SimulatedDataset:
    def __init__(self, n_samples: int=1000):
        """Creates a simulated data for maintenance cost and condition

        Parameters
        ----------
            n_samples : number of data samples to generate

        Returns
        -------
            data : pandas.DataFrame

        Usage:
        ------
            n_samples = 1000
            dataset = SimulatedDataset(n_samples=n_samples)
            data = dataset.generate()
        """
        self.n_samples = n_samples
        
    def generate(self) -> pd.DataFrame:
        """Generates the simulated data
        """
        age = np.random.randint(0, 100, self.n_samples)
        material = np.random.choice([0, 1, 2], self.n_samples, p=[0.3, 0.5, 0.2]) 
        size = np.random.randint(40, 200, self.n_samples)
        tenant_behavior = np.random.randint(1, 6, self.n_samples)
        maintenance_freq = np.random.randint(0, 5, self.n_samples)
        budget_constraints = np.random.choice([0, 1], self.n_samples, p=[0.6, 0.4]) 
        prev_maintenance_quality = np.random.choice([0, 1, 2], self.n_samples, p=[0.25, 0.55, 0.2])
        bathrooms = np.random.randint(1, 5, self.n_samples)
        location = np.random.choice(['Urban', 'Suburban', 'Rural'], self.n_samples, p=[0.5, 0.3, 0.2])
        has_garage = np.random.choice([0, 1], self.n_samples, p=[0.4, 0.6])
        rooms = np.random.randint(1, 7, self.n_samples)  # Assuming between 1 and 6 rooms

        # maintenance cost
        maintenance_cost = (age * 15.0) - (material * 100.0) + (size * 10.0) + \
                   (tenant_behavior * 50.0) - (maintenance_freq * 70.0) + \
                   (budget_constraints * 300.0) - (prev_maintenance_quality * 80.0) + \
                   (bathrooms * 120.0) + (has_garage * 200.0) + (rooms * 100.0)  # Rooms add to the cost

        # condition
        condition = 10 + (age * -0.1) + (material * -2.0) + (size * 0.02) + \
            (tenant_behavior * 1.4) - (maintenance_freq * 1.8) + \
            (budget_constraints * 4.0) + (prev_maintenance_quality * 1.4) - \
            (bathrooms * 1.0) + (has_garage * 2.0) - (rooms * 0.8)

        
        condition[location == 'Urban'] -= 2
        condition[location == 'Rural'] += 2

        condition = np.clip(condition, 1, 5)
        condition = np.round(condition).astype(int)  
        
        data = pd.DataFrame({
            'age': age,
            'material': material,
            'size': size,
            'tenant_behavior': tenant_behavior,
            'maintenance_frequency': maintenance_freq,
            'budget_constraints': budget_constraints,
            'previous_maintenance_quality': prev_maintenance_quality,
            'bathrooms': bathrooms,
            'location': location,
            'has_garage': has_garage,
            'rooms': rooms,
            'maintenance_cost': maintenance_cost,
            'house_condition': condition
        })
        return data

if __name__ == '__main__':
    # Test the dataset
    n_samples = 5
    dataset = SimulatedDataset(n_samples=n_samples)
    sample_data = dataset.generate()
    print(sample_data)