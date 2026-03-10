using Microsoft.AspNetCore.Mvc;
using InfraMonitorAPI.Models;

namespace InfraMonitorAPI.Controllers
{
    [ApiController]
    [Route("api/[controller]")]
    public class ServicesController : ControllerBase
    {
        private static List<Service> services = new List<Service>();

        [HttpGet]
        public IActionResult Get()
        {
            return Ok(services);
        }

        [HttpPost]
        public IActionResult Add(Service service)
        {
            services.Add(service);
            return Ok(service);
        }
    }
}