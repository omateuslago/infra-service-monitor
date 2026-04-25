using Microsoft.AspNetCore.Mvc;
using Microsoft.EntityFrameworkCore;
using InfraMonitorAPI.Database;
using InfraMonitorAPI.Models;

namespace InfraMonitorAPI.Controllers
{
    [ApiController]
    [Route("api/[controller]")]
    public class ChecksController : ControllerBase
    {
        private readonly AppDbContext _context;

        public ChecksController(AppDbContext context)
        {
            _context = context;
        }

        [HttpGet]
        public IActionResult Get()
        {
            var checks = _context.ServiceChecks
                .Include(x => x.Service)
                .OrderByDescending(x => x.CheckedAt)
                .Take(20)
                .ToList();

            return Ok(checks);
        }

        [HttpPost]
        public IActionResult Add(ServiceCheck check)
        {
            _context.ServiceChecks.Add(check);
            _context.SaveChanges();

            return Ok(check);
        }
    }
}