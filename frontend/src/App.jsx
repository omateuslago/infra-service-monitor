import { useEffect, useState } from "react";
import "./App.css";

const API_URL = "http://localhost:5000/api";

export default function App() {
  const [services, setServices] = useState([]);
  const [checks, setChecks] = useState([]);
  const [form, setForm] = useState({ name: "", url: "" });

  async function loadData() {
    const servicesResponse = await fetch(`${API_URL}/services`);
    const checksResponse = await fetch(`${API_URL}/checks`);

    setServices(await servicesResponse.json());
    setChecks(await checksResponse.json());
  }

  async function addService(e) {
    e.preventDefault();

    await fetch(`${API_URL}/services`, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(form),
    });

    setForm({ name: "", url: "" });
    loadData();
  }

  useEffect(() => {
    loadData();

    const interval = setInterval(loadData, 10000);
    return () => clearInterval(interval);
  }, []);

  const onlineCount = checks.filter((check) => check.isOnline).length;
  const offlineCount = checks.filter((check) => !check.isOnline).length;

  return (
    <main className="app">
      <section className="header">
        <div>
          <p className="eyebrow">Infra Service Monitor</p>
          <h1>Dashboard de monitoramento</h1>
          <p className="subtitle">
            Visualize serviços cadastrados, status recentes e tempo de resposta.
          </p>
        </div>

        <div className="status-pill">Auto refresh: 10s</div>
      </section>

      <section className="cards">
        <div className="card">
          <span>Serviços</span>
          <strong>{services.length}</strong>
        </div>

        <div className="card">
          <span>Online</span>
          <strong className="green">{onlineCount}</strong>
        </div>

        <div className="card">
          <span>Offline</span>
          <strong className="red">{offlineCount}</strong>
        </div>
      </section>

      <section className="grid">
        <div className="panel">
          <h2>Serviços monitorados</h2>

          <div className="list">
            {services.map((service) => (
              <div className="service-item" key={service.id}>
                <div>
                  <strong>{service.name}</strong>
                  <p>{service.url}</p>
                </div>

                <span className={service.isActive ? "badge active" : "badge"}>
                  {service.isActive ? "Ativo" : "Inativo"}
                </span>
              </div>
            ))}
          </div>
        </div>

        <div className="panel">
          <h2>Adicionar serviço</h2>

          <form onSubmit={addService} className="form">
            <input
              placeholder="Nome do serviço"
              value={form.name}
              onChange={(e) => setForm({ ...form, name: e.target.value })}
              required
            />

            <input
              placeholder="URL ex: https://google.com"
              value={form.url}
              onChange={(e) => setForm({ ...form, url: e.target.value })}
              required
            />

            <button type="submit">Adicionar</button>
          </form>
        </div>
      </section>

      <section className="panel">
        <h2>Últimos checks</h2>

        <div className="table">
          {checks.map((check) => (
            <div className="row" key={check.id}>
              <span>{check.service?.name ?? `Serviço #${check.serviceId}`}</span>

              <span className={check.isOnline ? "green" : "red"}>
                {check.isOnline ? "Online" : "Offline"}
              </span>

              <span>{check.responseTimeMs}ms</span>

              <span>{new Date(check.checkedAt).toLocaleString("pt-BR")}</span>
            </div>
          ))}
        </div>
      </section>
    </main>
  );
}