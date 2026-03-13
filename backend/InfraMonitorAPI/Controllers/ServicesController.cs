using Microsoft.AspNetCore.Mvc;
using InfraMonitorAPI.Models;
using InfraMonitorAPI.Database;

namespace InfraMonitorAPI.Controllers
{
    [ApiController]
    [Route("api/[controller]")]
    public class ServicesController : ControllerBase
    {
        private readonly AppDbContext _context;

        public ServicesController(AppDbContext context)
        {
            _context = context;
        }

        [HttpGet]
        public IActionResult Get()
        {
            var services = _context.Services.ToList();
            return Ok(services);
        }

        [HttpPost]
        public IActionResult Add(Service service)
        {
            _context.Services.Add(service);
            _context.SaveChanges();
            return Ok(service);
        }
    }
}