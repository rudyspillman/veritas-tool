import React, { useState } from 'react';
import { AnalysisStatus, MediaType, VerificationResult, AnalysisRequest } from './types';
import { verifyContent } from './services/gemini';
import AnalysisForm from './components/AnalysisForm';
import AnalysisResults from './components/AnalysisResults';
import SignalVisualizer from './components/SignalVisualizer';
import { Shield, Lock, Eye, AlertOctagon } from 'lucide-react';

const App: React.FC = () => {
  const [status, setStatus] = useState<AnalysisStatus>(AnalysisStatus.IDLE);
  const [result, setResult] = useState<VerificationResult | null>(null);
  const [error, setError] = useState<string | null>(null);

  const handleAnalysisRequest = async (request: AnalysisRequest) => {
    setStatus(AnalysisStatus.ANALYZING);
    setError(null);
    setResult(null);

    try {
      const verificationResult = await verifyContent(request.type, request.content, request.mimeType);
      setResult(verificationResult);
      setStatus(AnalysisStatus.COMPLETE);
    } catch (err) {
      console.error(err);
      setError("Analysis failed. Please try again or check your API key/connection.");
      setStatus(AnalysisStatus.ERROR);
    }
  };

  const resetAnalysis = () => {
    setStatus(AnalysisStatus.IDLE);
    setResult(null);
    setError(null);
  };

  // URL DE TU IMAGEN
  const backgroundUrl = "https://i.postimg.cc/Kzv816Jc/VERITAS_AI_Universal_Verification_Engine_IMAGEN.png";

  return (
    <div className="min-h-screen text-slate-100 font-sans selection:bg-veritas-500/30 relative">
      
      {/* --- FONDO PERSONALIZADO RUDY --- */}
      <div className="fixed inset-0 pointer-events-none z-0">
        {/* 1. La Imagen de Fondo */}
        <div 
          className="absolute inset-0 bg-cover bg-center bg-no-repeat"
          style={{ backgroundImage: `url(${backgroundUrl})` }}
        />
        {/* 2. Capa Oscura (Overlay) para que se lea el texto y los botones resalten */}
        <div className="absolute inset-0 bg-slate-950/70" />
      </div>

      {/* --- CABECERA --- */}
      <header className="relative z-10 border-b border-slate-800/50 bg-slate-950/60 backdrop-blur-md sticky top-0">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 h-20 flex items-center justify-between">
          <div className="flex items-center gap-3">
            <div className="bg-indigo-600/90 p-2 rounded-lg shadow-lg shadow-indigo-500/20">
              <Shield className="w-6 h-6 text-white" />
            </div>
            <div>
              <h1 className="text-xl font-bold tracking-tight text-white">VERITAS <span className="text-indigo-400">AI</span></h1>
              <p className="text-[10px] text-slate-300 uppercase tracking-widest font-mono">Universal Verification System</p>
            </div>
          </div>
          <div className="hidden md:flex items-center gap-6 text-sm text-slate-300 font-medium">
             <span className="flex items-center gap-2 hover:text-indigo-400 transition-colors cursor-default"><Eye className="w-4 h-4" /> Deepfake Detection</span>
             <span className="flex items-center gap-2 hover:text-indigo-400 transition-colors cursor-default"><Lock className="w-4 h-4" /> Fraud Prevention</span>
          </div>
        </div>
      </header>

      {/* --- CONTENIDO PRINCIPAL --- */}
      <main className="relative z-10 max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-12">
        
        {status === AnalysisStatus.IDLE && (
          <div className="text-center mb-12 animate-fade-in-up">
            <h2 className="text-4xl md:text-5xl font-black text-white mb-6 tracking-tight drop-shadow-lg">
              Truth in the Age of AI
            </h2>
            <p className="text-lg md:text-xl text-slate-300 max-w-2xl mx-auto mb-8 leading-relaxed drop-shadow-md">
              Instantly verify the authenticity of documents, images, audio, and video. 
              Detect deepfakes and manipulation with enterprise-grade forensic AI.
            </p>
          </div>
        )}

        <div className="flex flex-col items-center">
          {/* Formulario de Análisis */}
          {status === AnalysisStatus.IDLE && (
             <div className="w-full max-w-3xl bg-slate-950/40 backdrop-blur-sm p-6 rounded-2xl border border-slate-700/50 shadow-2xl">
                <AnalysisForm onSubmit={handleAnalysisRequest} isAnalyzing={false} />
             </div>
          )}

          {/* Estado Analizando */}
          {status === AnalysisStatus.ANALYZING && (
            <div className="w-full max-w-2xl text-center space-y-8 animate-pulse bg-slate-950/50 p-10 rounded-3xl backdrop-blur-md border border-indigo-500/30">
               <h3 className="text-2xl font-mono text-indigo-400">PROCESSING NEURAL ANALYSIS</h3>
               <SignalVisualizer isActive={true} />
               <p className="text-slate-400">Scanning for artifacts, metadata inconsistencies, and generative patterns...</p>
            </div>
          )}

          {/* Resultados */}
          {status === AnalysisStatus.COMPLETE && result && (
            <AnalysisResults result={result} onReset={resetAnalysis} />
          )}

          {/* Error */}
          {status === AnalysisStatus.ERROR && (
            <div className="max-w-md w-full bg-red-950/80 backdrop-blur-md border border-red-900 rounded-xl p-8 text-center space-y-4 shadow-2xl">
              <AlertOctagon className="w-16 h-16 text-red-500 mx-auto" />
              <h3 className="text-xl font-bold text-red-400">Analysis Error</h3>
              <p className="text-slate-300">{error}</p>
              <button 
                onClick={resetAnalysis}
                className="mt-4 px-6 py-2 bg-red-900 hover:bg-red-800 text-white rounded-lg transition-colors font-semibold"
              >
                Try Again
              </button>
            </div>
          )}
        </div>
      </main>
      
      <footer className="relative z-10 border-t border-slate-800/50 mt-20 bg-slate-950/80 backdrop-blur-md">
        <div className="max-w-7xl mx-auto px-4 py-8 text-center text-slate-500 text-sm">
          <p>© {new Date().getFullYear()} VERITAS AI. Universal Verification Engine.</p>
        </div>
      </footer>
    </div>
  );
};

export default App;
