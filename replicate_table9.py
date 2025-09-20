import numpy as np
import networkx as nx
from scipy.linalg import inv
from scipy.stats import kendalltau

def compute_katz_centrality(A, alpha, use_abs=False):
    """
    Compute Katz centrality for a given adjacency matrix and alpha value
    
    Parameters:
    A: Adjacency matrix
    alpha: Attenuation factor
    use_abs: Whether to use absolute values (for alpha >= 1/λ_max)
    
    Returns:
    Katz centrality vector
    """
    n = A.shape[0]
    I = np.eye(n)
    
    if use_abs:
        # For α >= 1/λ_max, use absolute value of inverse
        katz_matrix = np.abs(inv(I - alpha * A))
    else:
        # For α < 1/λ_max, standard Katz centrality
        katz_matrix = inv(I - alpha * A)
    
    # Katz centrality is the row sum of the Katz matrix
    return np.sum(katz_matrix, axis=1)

def compute_table7_values(n, m_values, num_samples=5):
    """
    Compute Kendall correlation coefficients for different Katz centrality measures
    
    Parameters:
    n: Number of nodes
    m_values: List of m values (number of attachments)
    num_samples: Number of random networks to generate for each m
    
    Returns:
    Dictionary with Kendall correlation coefficients
    """
    results = {}
    
    for m in m_values:
        print(f"Computing for m = {m}")
        tau_k1k2_list = []
        tau_k1k3_list = []
        tau_k1k4_list = []
        tau_k3k4_list = []
        
        for _ in range(num_samples):
            # Generate Barabási-Albert network
            G = nx.barabasi_albert_graph(n, m)
            A = nx.adjacency_matrix(G).todense()
            
            # Compute largest eigenvalue
            eigenvalues = np.linalg.eigvals(A)
            lambda_max = np.max(np.real(eigenvalues))
            
            # Define alpha values
            alpha1 = 0.1 / lambda_max
            alpha2 = 0.8 / lambda_max
            alpha3 = 1.5 / lambda_max
            alpha4 = 10.0 / lambda_max
            
            # Compute Katz centrality for different alpha values
            k1 = compute_katz_centrality(A, alpha1)
            k2 = compute_katz_centrality(A, alpha2)
            k3 = compute_katz_centrality(A, alpha3, use_abs=True)
            k4 = compute_katz_centrality(A, alpha4, use_abs=True)
            
            # Compute Kendall correlation coefficients
            tau_k1k2, _ = kendalltau(k1, k2)
            tau_k1k3, _ = kendalltau(k1, k3)
            tau_k1k4, _ = kendalltau(k1, k4)
            tau_k3k4, _ = kendalltau(k3, k4)
            
            tau_k1k2_list.append(tau_k1k2)
            tau_k1k3_list.append(tau_k1k3)
            tau_k1k4_list.append(tau_k1k4)
            tau_k3k4_list.append(tau_k3k4)
        
        # Average over samples
        results[m] = {
            'τ(k₁,k₂)': np.mean(tau_k1k2_list),
            'τ(k₁,k₃)': np.mean(tau_k1k3_list),
            'τ(k₁,k₄)': np.mean(tau_k1k4_list),
            'τ(k₃,k₄)': np.mean(tau_k3k4_list)
        }
    
    return results

# Parameters from Table 7
n = 200
m_values = [1, 2, 3, 5, 6, 7, 8, 10, 15, 40]

# Compute the Kendall correlation coefficients
results = compute_table7_values(n, m_values)

# Display results in table format
print("\nTable 7: Kendall coefficients for generalized Katz centrality")
print("=" * 85)
print(f"{'Network':<12} {'τ(k₁,k₂)':<10} {'τ(k₁,k₃)':<10} {'τ(k₁,k₄)':<10} {'τ(k₃,k₄)':<10}")
print("-" * 85)

for m in m_values:
    network = f"({n},{m})"
    tau_k1k2 = results[m]['τ(k₁,k₂)']
    tau_k1k3 = results[m]['τ(k₁,k₃)']
    tau_k1k4 = results[m]['τ(k₁,k₄)']
    tau_k3k4 = results[m]['τ(k₃,k₄)']
    
    print(f"{network:<12} {tau_k1k2:<10.3f} {tau_k1k3:<10.3f} {tau_k1k4:<10.3f} {tau_k3k4:<10.3f}")

print("=" * 85)
