import React, { useEffect, useState } from 'react';
import { useParams } from 'react-router-dom';
import api from '../services/api';

const DocumentDetails = () => {
  const { id } = useParams();
  const [doc, setDoc] = useState(null);

  useEffect(() => {
    api.get(`/documents/${id}`)
      .then(res => setDoc(res.data))
      .catch(() => alert('Error fetching document'));
  }, [id]);

  const highlightEntities = (text, entities) => {
    let highlighted = text;
    entities.forEach(ent => {
      // Escape special chars in entity name for regex
      const safeName = ent.name.replace(/[.*+?^${}()|[\]\\]/g, '\\$&');
      const regex = new RegExp(`(${safeName})`, 'gi');
      highlighted = highlighted.replace(regex, `<a href="${ent.url}" target="_blank" style="color:blue; text-decoration:underline;">$1</a>`);
    });
    return highlighted;
  };

  if (!doc) return <p>Loading...</p>;

  const { processo, relator, tribunal, decisao, data, descritores, sumario, content, Entities } = doc;
  const dateStr = data ? new Date(data).toLocaleDateString() : '';
  const finalContent = Entities && Entities.length > 0 ? highlightEntities(content, Entities) : content;

  return (
    <div>
      <h1>{tribunal} - {processo}</h1>
      <table border="1" cellPadding="5" style={{ borderCollapse: 'collapse', marginBottom: '20px' }}>
        <tbody>
          <tr><th>Processo</th><td>{processo}</td></tr>
          <tr><th>Relator</th><td>{relator}</td></tr>
          <tr><th>Tribunal</th><td>{tribunal}</td></tr>
          <tr><th>Decisão</th><td>{decisao}</td></tr>
          <tr><th>Data</th><td>{dateStr}</td></tr>
          <tr><th>Descritores</th><td>{descritores}</td></tr>
          <tr><th>Sumário</th><td>{sumario}</td></tr>
        </tbody>
      </table>
      <div dangerouslySetInnerHTML={{ __html: finalContent }} />
    </div>
  );
};

export default DocumentDetails;