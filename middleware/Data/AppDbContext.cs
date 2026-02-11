using Microsoft.EntityFrameworkCore;
using middleware.Models;

namespace middleware.Data
{
    public class AppDbContext : DbContext
    {
        public AppDbContext(DbContextOptions<AppDbContext> options)
            : base(options) { }

        public DbSet<Evento> Eventos { get; set; }
    }
}
