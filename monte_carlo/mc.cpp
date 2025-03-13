// a C++ program to perform a Monte Carlo
// compilation: g++ mc.cpp -o mc.x -O2
// execution: ./mc.x 
// saves MC trajectory to file trajectory.xyz
// saves MC energies time series to energy.dat

#include <iostream>
#include <fstream>
#include <vector>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <random>
#include <sstream>
#include <string>
#include <getopt.h>

using namespace std;

struct Config {
  int N = 512; // Number of particles
  double rho = 0.0210351; // Default number density in atoms / A3
  double T = 87.3; // Temperature in K
  double epsilon = 0.997; // Lennard-Jones well depth in kJ
  double sigma = 3.4; // Lennard-Jones sigma in angstroms
  int MC_STEPS = 1000000; // Monte Carlo steps
  int SKIP_STEPS=1000;
  double step_size=0.3;
  double box_length;
  int randseed=100269626; // replace this with your student number
};

void parseArguments(int argc, char* argv[], Config &config) {
  int opt;
  while ((opt = getopt(argc, argv, "N:r:T:e:s:M:E:")) != -1) {
    switch (opt) {
    case 'N': config.N = atoi(optarg); break;
    case 'r': config.rho = atof(optarg); break;
    case 'T': config.T = atof(optarg); break;
    case 'e': config.epsilon = atof(optarg); break;
    case 's': config.sigma = atof(optarg); break;
    case 'M': config.MC_STEPS = atoi(optarg); break;
    case 'k': config.SKIP_STEPS = atoi(optarg); break;
      
    default:
      cerr << "Usage: ./lj_simulation -N [particles] -r [density] -T [K] -e [kJ] -s [A] -M [steps] -E [eq_steps]\n";
      exit(EXIT_FAILURE);
    }
  }
}


double lennard_jones2(double r2, double epsilon, double s6)
{
  double sr6 = s6/(r2*r2*r2);
  return 4 * epsilon * (sr6 * sr6 - sr6); // Energy in kJ
}

void initialize_fcc(vector<vector<double>> &positions, double box_length )
{
  int cells_per_side = 8; // 8x8x8 FCC lattice
  double cell_length = box_length / cells_per_side;
  int idx = 0;

  for (int x = 0; x < cells_per_side; ++x)
    {
      for (int y = 0; y < cells_per_side; ++y)
	{
	  for (int z = 0; z < cells_per_side; ++z)
	    {
	      if (idx >= positions.size()) return;
	      int sum=x+y+z;
	      
	      // FCC basis
	      if( (sum%2)==0)
		positions[idx++] = {x * cell_length, y * cell_length, z * cell_length};
	      else
		positions[idx++] = { (x+0.5) * cell_length, (y+0.5) * cell_length, (z+0.5) * cell_length};
	    }
	}
    }
}

double total_energy(const vector<vector<double>>& positions, const Config& config) {
    double E = 0.0;
    double cutoff=2.5*config.sigma;
    double cutoff2=cutoff*cutoff;
    double s6=pow(config.sigma, 6);
    
    for (int i = 0; i < config.N - 1; ++i)
      {
        for (int j = i + 1; j < config.N; ++j)
	  {
            double r2 = 0.0;
            for (int d = 0; d < 3; ++d)
	      {
                double dx = positions[i][d] - positions[j][d];
                dx -= config.box_length * round(dx / config.box_length); // Periodic boundary
                r2 += dx * dx;
	      }
	    
            if (r2 < cutoff2) // Cutoff distance
	      E += lennard_jones2(r2, config.epsilon, s6);
	  }
      }
    return E;
}

void metropolis_mc(Config &config)
{
    config.box_length = pow(config.N / config.rho, 1.0 / 3.0);
    cout << "cell_length " << config.box_length << endl;
    vector<vector<double>> positions(config.N, vector<double>(3));
    default_random_engine rng(config.randseed);
    uniform_real_distribution<double> dist(0, config.box_length);
    uniform_real_distribution<double> move_dist(-config.step_size, config.step_size);
    uniform_real_distribution<double> accept_dist(0, 1);

    initialize_fcc(positions, config.box_length);
    
    int rejected_moves = 0;
    int accepted_moves = 0, total_moves = 0;
    double k_B = 0.008314; // kJ/(mol*K)
    double beta = 1.0 / (k_B * config.T);

    ofstream energy_file("energy.dat");
    ofstream xyz_file("trajectory.xyz");
    
    for (int step = 0; step < config.MC_STEPS; ++step)
      {
        int i = rng() % config.N;
        vector<double> old_pos = positions[i];

        double old_energy = total_energy(positions, config);
        for (int d = 0; d < 3; ++d)
            positions[i][d] += move_dist(rng);
	
        double new_energy = total_energy(positions, config);
        double delta_E = new_energy - old_energy;
	  
        if (delta_E > 0 && exp(-beta * delta_E) < accept_dist(rng))
	  {
	    ++rejected_moves;
	    positions[i] = old_pos; // Reject move
	  }
	else
	  {
            ++accepted_moves;
	  }
        ++total_moves;

        if ((step % config.SKIP_STEPS) == 0)
	  {
	    cout << "Step " << step << endl;
	    energy_file << step << " " << new_energy << endl;
            xyz_file << config.N << "\nStep " << step << endl;
            for (const auto &p : positions)
	      xyz_file << "Ar " << p[0] << " " << p[1] << " " << p[2] << endl;
	  }
	
      }

    energy_file.close();
    xyz_file.close();

    double acceptance_ratio = static_cast<double>(accepted_moves) / total_moves;
    cout << "Accepted Moves: " << accepted_moves << endl;
    cout << "Rejected Moves: " << rejected_moves << endl;
    
    cout << "Acceptance Ratio: " << acceptance_ratio << endl;
}

int main(int argc, char* argv[])
{
    Config config;
    parseArguments(argc, argv, config);
    metropolis_mc(config);
    return 0;
}

