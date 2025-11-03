
%global baseurl https://storage.googleapis.com/claude-code-dist-86c565f3-f756-42ad-8dfa-d59b1c096819/claude-code-releases

%{!?_version:%define _version %(curl -sL %{baseurl}/stable 2>/dev/null || echo "2.0.31")}

Name:           claude
Version:        %{_version}
Release:        2%{?dist}
Summary:        Claude Code

License:        Proprietary
URL:            https://claude.ai

%ifarch x86_64
%global claude_arch linux-x64
%endif
%ifarch aarch64
%global claude_arch linux-arm64
%endif

Source0:  %{baseurl}/%{version}/%{claude_arch}/claude
Source10: claude-wrapper

%description
Claude Code is an agentic coding tool that lives in your terminal, understands your codebase, and helps you code faster by executing routine tasks, explaining complex code, and handling git workflows -- all through natural language commands.

%prep

%build

%install
%{__rm} -rf %{buildroot}
%{__mkdir_p} %{buildroot}%{_bindir}

%{__mkdir_p} %{buildroot}%{_libexecdir}/%{name}
%{__install} -m 0644 %{SOURCE0}  %{buildroot}%{_libexecdir}/claude
%{__install} -m 0644 %{SOURCE10} %{buildroot}%{_bindir}/claude

%files
%{_bindir}/claude
%dir %{_libexecdir}/claude
%{_libexecdir}/claude/claude

%changelog
* Sat Nov 01 2025 KOSHIKAWA Kenichi <reishoku.misc@pm.me> - 2.0.31-2
- Disable telemetry related environmental variables
- Add aarch64 GitHub Actions workflow for CI

* Sat Nov 01 2025 KOSHIKAWA Kenichi <reishoku.misc@pm.me> - 2.0.31-1
- Initial RPM package for Claude Code
