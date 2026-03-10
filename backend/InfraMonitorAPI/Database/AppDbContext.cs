using Microsoft.EntityFrameworkCore;
using InfraMonitorAPI.Models;

namespace InfraMonitorAPI.Database
{
    public class AppDbContext : DbContext
    {
        public AppDbContext(DbContextOptions<AppDbContext> options)
            : base(options)
        {
        }

        public DbSet<Service> Services { get; set; }
    }
}